# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**hiveio-schemas** is a Python library for validating and serializing Hive blockchain JSON data. It provides
msgspec-based field types of Hive data (accounts, assets, keys, integers, time...), the validation of data against
models with these types and the base class of such models.

Models of API responses, operations and transactions are not kept here - they are generated in the `hiveio_api` package
(hive repo): API responses from `openapi.json`, operations from the description of operations produced by the build of
hived. Its validation models use the field types of this package (`schemas/fields/base_type_mappings.py`).

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
- Handles automatic type swapping in `__post_init__` for special Hive types
- Supports dictionary-like access via `__getitem__`/`__setitem__`

**Serialization Formats** - fixed by the type, never chosen at runtime:
- **HF26** (current): NAI-based asset format `{"amount": "1000", "precision": 3, "nai": "@@000000021"}` (`AssetHive`, ...)
- **Legacy**: String-based asset format `"1.000 HIVE"` (`LegacyAssetHive`, ...)

### Key Modules

- **`schemas/fields/`**: Custom field types (assets, AccountName, PublicKey, HiveDateTime, etc.)
  - `base_type_mappings.py`: builtin aliases of the field types (`AccountName = str`, ...) used by generated public API
    models, plus `BASE_TYPE_MAPPINGS` (alias name -> validating type import path) used by generated validation models.
    Must stay import-light (no msgspec).
- **`schemas/validation.py`**: Validation of JSON data (builtins) against msgspec models with Hive types -
  `validate(data, model)` returning `list[SchemaError]` (with paths), plus
  `is_matching_model(value, field_type)` / `validate_schema_field(value, field_type)` for single values. Generic, knows
  nothing about APIs - endpoints, the registry of validation models and JSON-RPC handling live in `hiveio_api` (hive
  repo).
- **`schemas/errors.py`**: All exceptions defined by the package (deriving from `SchemaBaseError`) plus aliases of msgspec
  `ValidationError`/`DecodeError`. New exceptions go here, not to the modules raising them. Field types report invalid values with `FieldValidationError` - it is a msgspec
  `ValidationError` (one exception type for invalid data) and a `ValueError` (msgspec adds the location
  `- at $.path` only to `ValueError`/`TypeError` raised by validators).
- **`schemas/decoders.py`** / **`schemas/encoders.py`**: msgspec hooks (`dec_hook_hf26`, `get_hf26_decoder`,
  `enc_hook_hf26`, `get_hf26_encoder`). Field types unknown to msgspec derive from `Serializable`
  (`schemas/fields/serializable.py`) - they decode themselves with `deserialize` (by default the constructor) and encode
  with `serialize`, always in the form given by their type. Values of any JSON type are annotated `object` (`Any` is
  not used in typing) - `dec_hook_hf26` keeps them as they are
- **`schemas/_json_schema.py`**: JSON Schema generation (`PreconfiguredBaseModel.schema_json()`, `schema_hook`)
- **`schemas/policies/`**: Runtime policies for extra fields, testnet assets, etc.

### Custom Field Types

Defined in `schemas/fields/`:
- **Assets** (`assets/_base.py`) - the type decides the JSON form:
  - NAI form: `AssetHive`, `AssetHbd`, `AssetVests`, unions `AssetHiveOrHbd`, `AssetHiveOrVests`, `AnyAsset`
  - legacy form: `LegacyAssetHive`, `LegacyAssetHbd`, `LegacyAssetVests`, unions `LegacyAssetHiveOrHbd`,
    `LegacyAssetHiveOrVests`, `LegacyAnyAsset` (testnet symbols are kept - `LegacyAssetTests`, `LegacyAssetTbd`)
  - msgspec allows only one custom type in a union and requires a decoded value to be an instance of the declared type,
    so unions are base classes of their members (`AssetHive` is an `AssetHiveOrHbd`); `asset.as_legacy_asset()` converts
    to the legacy form
- **`JsonString`** (`json_string.py`): JSON embedded in a string (`custom_json`)
- **Validators**: `AccountName`, `PublicKey`, `Permlink` with regex constraints
- **Integers**: `HiveInt`, `Uint16t`, `Uint32t`, `Int64t`, `Uint64t`
- **Time and hashes**: `HiveDateTime`, `Signature`, `TransactionId`

## Python Version

Requires Python 3.12+. CI runs on Python 3.14.
