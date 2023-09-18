from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


from schemas.apis.account_by_key_api import response_schemas as account_by_key_api  # noqa: F401
from schemas.apis.account_history_api import response_schemas as account_history_api  # noqa: F401
from schemas.apis.block_api import response_schemas as block_api  # noqa: F401
from schemas.apis.condenser_api import response_schemas as condenser_api  # noqa: F401
from schemas.apis.database_api import response_schemas as database_api  # noqa: F401
from schemas.apis.debug_node_api import response_schemas as debug_node_api  # noqa: F401
from schemas.apis.jsonrpc import response_schemas as jsonrpc  # noqa: F401
from schemas.apis.market_history_api import response_schemas as market_history_api  # noqa: F401
from schemas.apis.network_broadcast_api import response_schemas as network_broadcast_api  # noqa: F401
from schemas.apis.network_node_api import response_schemas as network_node_api  # noqa: F401
from schemas.apis.rc_api import response_schemas as rc_api  # noqa: F401
from schemas.apis.reputation_api import response_schemas as reputation_api  # noqa: F401
from schemas.apis.transaction_status_api import response_schemas as transaction_status_api  # noqa: F401
from schemas.apis.wallet_bridge_api import response_schemas as wallet_bridge_api  # noqa: F401

__locals = locals().copy()  # this is required, because creation of loop changes size of dict
apis = {key: value for key, value in __locals.items() if key.endswith("_api") or key in ["jsonrpc"]}


def get_schema(schema_name: str) -> type[PreconfiguredBaseModel]:
    def __snake_case_to_pascal_case(text: str) -> str:
        return "".join([segment.title() for segment in text.split("_")])

    api, method = schema_name.split(".")
    assert api in apis, f"Api `{api}` not found, currently supported are: {apis}"
    schemas_module = apis[api]

    method = __snake_case_to_pascal_case(method)
    try:
        return getattr(schemas_module, method)  # type: ignore[no-any-return]
    except ImportError as e:
        raise AttributeError(
            f"""The "{method}" method in "{api}" API does not have a matching schema.
This means that the schema does not exist.
Add "{method}" schema definition to {schemas_module.__file__}"""
        ) from e
