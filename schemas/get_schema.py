from __future__ import annotations

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from types import ModuleType

    from schemas._preconfigured_base_model import PreconfiguredBaseModel


from schemas.apis.account_by_key_api import response_schemas as account_by_key_api
from schemas.apis.account_history_api import response_schemas as account_history_api
from schemas.apis.block_api import response_schemas as block_api
from schemas.apis.condenser_api import response_schemas as condenser_api
from schemas.apis.database_api import response_schemas as database_api
from schemas.apis.debug_node_api import response_schemas as debug_node_api
from schemas.apis.jsonrpc import response_schemas as jsonrpc
from schemas.apis.market_history_api import response_schemas as market_history_api
from schemas.apis.network_broadcast_api import response_schemas as network_broadcast_api
from schemas.apis.network_node_api import response_schemas as network_node_api
from schemas.apis.rc_api import response_schemas as rc_api
from schemas.apis.reputation_api import response_schemas as reputation_api
from schemas.apis.transaction_status_api import response_schemas as transaction_status_api
from schemas.apis.wallet_bridge_api import response_schemas as wallet_bridge_api

__all__ = [
    "APIS",
    "get_schema",
]

APIS: Final[dict[str, ModuleType]] = {
    "account_by_key_api": account_by_key_api,
    "account_history_api": account_history_api,
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
}


def get_schema(schema_name: str) -> type[PreconfiguredBaseModel]:
    def __snake_case_to_pascal_case(text: str) -> str:
        return "".join([segment.title() for segment in text.split("_")])

    api, method = schema_name.split(".")
    assert api in APIS, f"Api `{api}` not found, currently supported are: {APIS}"
    schemas_module = APIS[api]

    method = __snake_case_to_pascal_case(method)
    try:
        return getattr(schemas_module, method)  # type: ignore[no-any-return]
    except ImportError as e:
        raise AttributeError(
            f"""The "{method}" method in "{api}" API does not have a matching schema.
This means that the schema does not exist.
Add "{method}" schema definition to {schemas_module.__file__}"""
        ) from e
