# hiveio-schemas

Python schemas for Hive blockchain JSON: operations, transactions, API responses, and related types.

The import package is `schemas`. Models are [msgspec](https://github.com/jcrist/msgspec) structs (`PreconfiguredBaseModel`), not JSON Schema / pydantic wrappers.

Requires **Python 3.12+**. Latest release: see [PyPI](https://pypi.org/project/hiveio-schemas/) and [GitLab tags](https://gitlab.syncad.com/hive/schemas/-/tags).

## Installation

From [PyPI](https://pypi.org/project/hiveio-schemas/) (tagged releases):

```bash
pip install hiveio-schemas
# or
poetry add hiveio-schemas
```

Pre-release / CI builds are also published to the Hive group Package Registry. With Poetry:

```toml
[[tool.poetry.source]]
name = "gitlab-hive"
url = "https://gitlab.syncad.com/api/v4/groups/136/-/packages/pypi/simple"
priority = "primary"
```

```bash
poetry add hiveio-schemas
```

With pip (project registry):

```bash
pip install hiveio-schemas \
  --index-url https://gitlab.syncad.com/api/v4/projects/362/packages/pypi/simple \
  --extra-index-url https://pypi.org/simple
```

### From source (development)

```bash
git clone https://gitlab.syncad.com/hive/schemas.git
cd schemas
python3 -m venv .venv && source .venv/bin/activate
poetry install
```

Editable install without Poetry:

```bash
pip install -e .
```

## Basic usage

Parse an operation (HF26 / NAI assets):

```python
from schemas.operations import TransferOperation

op = TransferOperation.parse_builtins({
    "from": "alice",
    "to": "bob",
    "amount": {"amount": "1000", "precision": 3, "nai": "@@000000021"},
    "memo": "",
})
print(op.json())  # serialize back to JSON string
```

Parse a JSON-RPC API response:

```python
from schemas.apis.block_api import GetBlock
from schemas.jsonrpc import get_response_model

model = get_response_model(GetBlock, raw_json_string, "hf26")  # or "legacy"
```

Look up a response schema by `"api.method"` name:

```python
from schemas.get_schema import get_schema

GetDynamicGlobalProperties = get_schema("database_api.get_dynamic_global_properties")
```

Model helpers: `.dict()`, `.json()`, `.parse_raw()`, `.parse_file()`, `.parse_builtins()`, `.copy()`, `.schema_json()`, `.humanize()`.

For callers that should not import msgspec directly, `schemas.convert` exposes `to_builtins`, `json_encode`, and `UNSET` (pass `enc_hook` from `schemas.encoders` when encoding Hive field types).

### Serialization formats

- **HF26** (current): NAI assets, e.g. `{"amount": "1000", "precision": 3, "nai": "@@000000021"}`; operations as `{ "type": "...", "value": {...} }`.
- **Legacy**: string assets, e.g. `"1.000 HIVE"`; operations often as `["transfer", {...}]`.

Decoders/encoders live in `schemas.decoders` and `schemas.encoders`. Use `get_response_model(..., "hf26"|"legacy")` or pass a custom decoder factory to `parse_raw` / `parse_file`.

## Package layout

| Path | Contents |
|------|----------|
| `schemas/operations/` | Blockchain operations (one module per op) |
| `schemas/operations/virtual/` | Virtual operations |
| `schemas/operations/representation_types.py` | HF26 / legacy representation wrappers (generated) |
| `schemas/apis/<api_name>/` | Request/response schemas per Hive API |
| `schemas/fields/` | Field types: assets, account names, keys, integers, datetimes, … |
| `schemas/transaction.py` | `Transaction` / `TransactionLegacy` and user-friendly variants |
| `schemas/jsonrpc.py` | JSON-RPC request/result helpers and `get_response_model` |
| `schemas/policies/` | Runtime policies (`set_policies`, testnet assets, extra fields, …) |
| `schemas/notifications/` | Beekeeper / node notification payloads |
| `schemas/convert.py` | `to_builtins`, `json_encode`, `UNSET` |
| `schemas/get_schema.py` | `get_schema("api.method")` registry |

APIs under `schemas/apis/` include, among others: `database_api`, `condenser_api`, `block_api`, `account_history_api`, `account_by_key_api`, `rc_api`, `market_history_api`, `network_broadcast_api`, `transaction_status_api`, `wallet_bridge_api`, `beekeeper_api`, `debug_node_api`, `reputation_api`, `network_node_api`, `app_status_api`, `jsonrpc`.

## Updating operations / representations

Operation classes live in `schemas/operations/` (and `virtual/`). After adding or renaming an operation that should appear in the HF26/legacy representation unions, regenerate the generated files:

```bash
python schemas/operations/generate_representation_types.py
python schemas/operations/virtual/generate_representation_types.py
```

Do not edit `representation_types.py` by hand; those files are overwritten by the generators.

## Development

```bash
poetry install
poetry run pytest tests/
poetry run mypy schemas/ tests/
poetry run ruff check --fix schemas/ tests/
poetry run ruff format schemas/ tests/
poetry run pre-commit run --all-files
```

Versioning uses `poetry-dynamic-versioning` from git tags (see `pyproject.toml`). Tagged builds are published to PyPI and the GitLab Package Registry from CI.

## Related Hive libraries

Consumed by and/or related to:

- [clive](https://gitlab.syncad.com/hive/clive) (`hiveio-clive`) — CLI/TUI wallet
- [wax](https://gitlab.syncad.com/hive/wax) (`hiveio-wax`) — bindings around Hive C++ logic
- [beekeeper](https://gitlab.syncad.com/hive/beekeeper) / `hiveio-beekeepy` — key/wallet service
- [test-tools](https://gitlab.syncad.com/hive/test-tools) (`hiveio-test-tools`) — test helpers
- [Hive](https://gitlab.syncad.com/hive/hive) — blockchain node

Repository: https://gitlab.syncad.com/hive/schemas
