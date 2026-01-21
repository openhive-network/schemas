# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**hiveio-schemas** is a Python library for validating and serializing Hive blockchain JSON data structures. It provides msgspec-based schema definitions for all Hive blockchain operations, API responses, and transactions.

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

**Serialization Formats**:
- **HF26** (current): NAI-based asset format `{"amount": "1000", "precision": 3, "nai": "@@000000021"}`
- **Legacy**: String-based asset format `"1.000 HIVE"`

### Key Modules

- **`schemas/operations/`**: All blockchain operations (transfer, vote, comment, etc.)
  - Each operation has its own file plus representation types in `representation_types.py`
  - Virtual operations are in `virtual/` subdirectory
- **`schemas/apis/`**: Response schemas for each Hive API (database_api, condenser_api, etc.)
- **`schemas/fields/`**: Custom field types (assets, AccountName, PublicKey, HiveDateTime, etc.)
- **`schemas/jsonrpc.py`**: JSON-RPC request/response handling with `get_response_model()`
- **`schemas/decoders.py`**: Decoding hooks for HF26 and legacy formats
- **`schemas/encoders.py`**: Encoding hooks for serialization
- **`schemas/policies/`**: Runtime policies for extra fields, testnet assets, etc.

### Custom Field Types

Defined in `schemas/fields/`:
- **Assets**: `AssetHive`, `AssetHbd`, `AssetVests` with NAI and legacy parsing
- **Validators**: `AccountName`, `PublicKey`, `Permlink` with regex constraints
- **Integers**: `HiveInt`, `Uint16t`, `Uint32t`, `Int64t`, `Uint64t`
- **Compound**: `HiveDateTime`, `Signature`, `TransactionId`

### Operation Representations

Operations have two forms:
- **Raw operations**: e.g., `TransferOperation` - the operation data itself
- **Representations**: Wrappers with `type` and `value` fields for HF26/Legacy serialization
  - `HF26RepresentationTransferOperation` wraps `TransferOperation` with `type="transfer_operation"`
  - `LegacyRepresentationTransferOperation` uses array format `["transfer", {...}]`

### Testing Pattern

Tests validate round-trip serialization:
```python
verify_serialization_and_deserialization(
    schema=ResponseSchema,
    parameters={"jsonrpc": "2.0", "result": {...}, "id": 1},
    serialization_type="hf26"  # or "legacy"
)
```

## Python Version

Requires Python 3.12+. CI runs on Python 3.14.
