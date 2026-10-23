# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**hiveio-schemas** is a Python library for validating and serializing Hive blockchain JSON data. It provides
msgspec-based field types of Hive data (accounts, assets, keys, integers, time...), the validation of data against
models with these types and the base class of such models.

Models of API responses, operations and transactions are not kept here - they are generated in the `hiveio_api` package
(hive repo): API responses from `openapi.json`, operations from the description of operations produced by the build of
hived. Its models use the field types of this package - public models `schemas.fields.public`, validation models
`schemas.fields.validation`.

## Development Commands

```bash
# Install dependencies
poetry install

# Run all tests
poetry run pytest tests/

# Run a specific test file
poetry run pytest tests/test_hive_fields.py

# Run tests with verbose output
poetry run pytest tests/ -v

# Type checking
poetry run mypy schemas/ tests/

# Linting (with auto-fix)
poetry run ruff check --fix schemas/ tests/

# Format code
poetry run ruff format schemas/ tests/

# Run pre-commit hooks (includes ruff, mypy, poetry-lock check)
poetry run pre-commit run --all-files
```

## Dependency Management (Poetry)

The lockfile pins exact versions of all dependencies (direct and transitive). This prevents dependency mismatches between environments - if the lockfile is wrong or missing, builds may fail or behave differently. These rules keep it synchronized with pyproject.toml.

- **Dependency versions are specified in `pyproject.toml` and locked in `poetry.lock`**
- **Always use `poetry lock`** (without additional flags like `--regenerate`)
- **Always run `poetry lock` after changing `pyproject.toml`**
- **The `poetry.lock` file must be in the repository** - never add it to `.gitignore`
- **Never delete `poetry.lock`** - it ensures reproducible builds
- **Never edit `poetry.lock` manually** - always use poetry commands
- **Don't upgrade dependencies on your own** - only upgrade when explicitly requested

## Architecture

### Core Classes

**`PreconfiguredBaseModel`** (`schemas/_preconfigured_base_model.py`):
- Base class for all schema types, extends `msgspec.Struct`
- Provides `dict()`, `json()`, `parse_raw()`, `parse_file()`, `parse_builtins()` methods
- Supports dictionary-like access via `__getitem__`/`__setitem__`

**Serialization Formats** - fixed by the type, never chosen at runtime:
- **HF26** (current): NAI-based asset format `{"amount": "1000", "precision": 3, "nai": "@@000000021"}` (`AssetHive`, ...)
- **Legacy**: String-based asset format `"1.000 HIVE"` (`LegacyAssetHive`, ...)

### Key Modules

- **`schemas/fields/`**: Field types of Hive data in three variants of one set of names, each in its own package -
  every user takes the types from one place (the package `__init__` stays import-light):
  - `validation/`: forms for validation models generated in `hiveio_api` and hand-written msgspec models - full
    validation by msgspec itself, no hooks: `Annotated[<builtin>, msgspec.Meta(...)]` (`AccountName`, `Uint16t`, ...),
    `int | Annotated[str, <pattern>]` for `HiveInt`, `Int64t`, `Uint64t` (hived sends big integers as strings), a
    string matching `HIVE_TIME_PATTERN` for `HiveDateTime`, plain `str` for `JsonString` (no pattern can check JSON),
    msgspec types of assets (`validation/_assets.py`).
  - `user_friendly/`: types checked only when created (`AccountName(".")` raises `FieldValidationError`), used by
    hand-written code: classes of builtins (`class AccountName(SimpleInitValidator, str, form=validation.AccountName)`,
    `_fields.py`, `_simple_init_validator.py`) checked by msgspec by the form of the same name (the rules are defined
    once, `meta()` gives them), `int` for `HiveInt`, `Int64t`, `Uint64t`, and the own types `Asset`, `HiveDateTime`,
    `JsonString`. The classes of builtins are not meant for msgspec models - hand-written models take the forms of
    `validation/` (`HiveDateTime`, `JsonString` are decoded there by the hooks).
  - `public/`: builtin aliases of the field types (`AccountName = str`, ...; `_fields.py`) used by generated public API
    models - no validation; every alias has its form of the same name in `validation/`. Also `Asset` (`_assets.py`) and
    the information about kinds of assets (`_asset_info.py`). Must stay import-light (no msgspec).
  - shared by the variants (their own JSON form, decoded by the hooks of hand-written models): `hive_datetime.py`,
    `json_string.py`, `serializable.py`.
- **`schemas/validation.py`**: Validation of JSON data (builtins) against msgspec models with Hive types -
  `validate(data, model)` returning `list[SchemaError]` (with paths), plus
  `is_matching_model(value, field_type)` for single values. Generic, knows
  nothing about APIs - endpoints, the registry of validation models and JSON-RPC handling live in `hiveio_api` (hive
  repo).
- **`schemas/errors.py`**: All exceptions defined by the package (deriving from `SchemaBaseError`) plus aliases of msgspec
  `ValidationError`/`DecodeError`. New exceptions go here, not to the modules raising them. Field types report invalid values with `FieldValidationError` - it is a msgspec
  `ValidationError` (one exception type for invalid data) and a `ValueError` (msgspec adds the location
  `- at $.path` only to `ValueError`/`TypeError` raised by validators).
- **`schemas/decoders.py`** / **`schemas/encoders.py`**: msgspec hooks (`dec_hook_hf26`, `get_hf26_decoder`,
  `enc_hook_hf26`, `get_hf26_encoder`) for hand-written models. Types unknown to msgspec derive from `Serializable`
  (`schemas/fields/serializable.py`, also used by other repositories; `HiveDateTime` only for now) - they decode with
  `deserialize` (by default the constructor) and encode with `serialize` (`HiveDateTime`, `JsonString`). Types of
  public models (`Asset`, `HiveDateTime`) are encoded by `to_builtins`. Values of any JSON type are annotated `object` (`Any` is not used in typing) -
  `dec_hook_hf26` keeps them as they are. msgspec builds the information about a type on its first use, which is not
  thread safe - decoders and conversions of models (`get_hf26_decoder`, `parse_builtins`, `validate`) use types within
  `first_use_guarded`
- **`schemas/_json_schema.py`**: JSON Schema generation (`PreconfiguredBaseModel.schema_json()`, `schema_hook`)

### Custom Field Types

Defined in `schemas/fields/`:
- **Information about kinds of assets** (`public/_asset_info.py`): literal types of NAIs and precisions
  (`HIVE_ASSET_NAI = Literal["@@000000021"]`, ...), `AssetInfo` and `HIVE_ASSET`, `HBD_ASSET`, `VESTS_ASSET` (taking
  the values of the literals) are the only definition of NAIs, precisions and symbols of assets - everything else
  (kinds of `Asset`, validating types, models generated in hiveio_api) refers to them or finds them with
  `asset_info_of_nai` / `asset_info_of_symbol`. Never repeat a NAI, symbol or precision of an asset elsewhere
  (`tests/unit/test_asset_info.py` checks the code). `token()` of assets, kinds and factories gives the information
  (displayed as the symbol of the network)
- **User-friendly assets** (`public/_assets.py`, exported by `schemas.fields.public` and
  `schemas.fields.user_friendly`): `Asset` of both JSON forms with its kinds and factories, `AssetNaiAmount` (alias of
  `int`, the amount of the NAI form)
- **Validating types of assets** (`validation/_assets.py`, exported by `schemas.fields.validation`) - only for
  validation models (generators refer to them by name), the type decides the JSON form and msgspec validates it without
  hooks:
  - NAI form: `AssetHive`, `AssetHbd`, `AssetVests`, unions `AssetHiveOrHbd`, `AssetHiveOrVests`, `AnyAsset` - frozen
    structs with the literals of `_asset_info` as types of `nai` and `precision`; unions are base classes of their members
    (`AssetHive` is an `AssetHiveOrHbd`) and check the NAI and the precision separately
  - legacy form: `LegacyAssetHive`, `LegacyAssetHbd`, `LegacyAssetVests`, unions `LegacyAssetHiveOrHbd`,
    `LegacyAssetHiveOrVests`, `LegacyAnyAsset` - `Annotated[str, Meta(pattern=...)]` of the amount with the precision
    of the kind and a symbol of the kind (testnet symbols too - `1.000 TESTS`)
  - amounts may be negative in both forms
- **`JsonString`** (`json_string.py`): JSON embedded in a string (`custom_json`), parsed when created
- **Types of builtins** (`validation/_fields.py`, `validation/_aliases.py` - the rules; `user_friendly/_fields.py` - the
  classes; `public/_fields.py` - the aliases):
  names and keys (`AccountName`, `PublicKey`, `Permlink`, ...), hashes (`Sha256`, `Signature`, `TransactionId`, ...),
  integers (`Uint8t` ... `Uint32t`); rules shared with other code are in `schemas/hive_constants.py`
- **Time**: `HiveDateTime` (`hive_datetime.py`, import-light)

## Python Version

Requires Python 3.12+. CI runs on Python 3.14.
