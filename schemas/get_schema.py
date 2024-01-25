from __future__ import annotations

from typing import TYPE_CHECKING, Final

from schemas._case import snake_case_to_pascal_case

if TYPE_CHECKING:
    from types import ModuleType

    from schemas._preconfigured_base_model import PreconfiguredBaseModel


from schemas.apis import (
    account_by_key_api,
    account_history_api,
    beekeeper_api,
    block_api,
    bridge_api,
    condenser_api,
    database_api,
    debug_node_api,
    jsonrpc,
    market_history_api,
    network_broadcast_api,
    network_node_api,
    rc_api,
    reputation_api,
    transaction_status_api,
    wallet_bridge_api,
)

__all__ = [
    "APIS",
    "get_schema",
]

APIS: Final[dict[str, ModuleType]] = {
    "account_by_key_api": account_by_key_api,
    "account_history_api": account_history_api,
    "beekeeper_api": beekeeper_api,
    "block_api": block_api,
    "condenser_api": condenser_api,
    "database_api": database_api,
    "debug_node_api": debug_node_api,
    "jsonrpc": jsonrpc,
    "market_history_api": market_history_api,
    "network_broadcast_api": network_broadcast_api,
    "network_node_api": network_node_api,
    "rc_api": rc_api,
    "reputation_api": reputation_api,
    "transaction_status_api": transaction_status_api,
    "wallet_bridge_api": wallet_bridge_api,
    "bridge": bridge_api,
}


def get_schema(schema_name: str) -> type[PreconfiguredBaseModel]:
    api, method = schema_name.split(".")
    assert api in APIS, f"Api `{api}` not found, currently supported are: {APIS}"
    schemas_module = APIS[api]

    method = snake_case_to_pascal_case(method)
    try:
        return getattr(schemas_module, method)  # type: ignore[no-any-return]
    except ImportError as e:
        raise AttributeError(
            f"""The "{method}" method in "{api}" API does not have a matching schema.
This means that the schema does not exist.
Add "{method}" schema definition to {schemas_module.__file__}"""
        ) from e
