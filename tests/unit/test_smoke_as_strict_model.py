from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

import schemas.account_by_key_api.response_schemas as account_by_key_api
import schemas.account_history_api.response_schemas as account_history_api
import schemas.block_api.response_schemas as block_api
import schemas.condenser_api.response_schemas as condenser_api
import schemas.database_api.response_schemas as database_api
import schemas.debug_node_api.response_schemas as debug_node_api
import schemas.jsonrpc.response_schemas as jsonrpc
import schemas.market_history_api.response_schemas as market_history_api
import schemas.network_broadcast_api.response_schemas as network_broadcast_api
import schemas.network_node_api.response_schemas as network_node_api
import schemas.rc_api.response_schemas as rc_api
import schemas.reputation_api.response_schemas as reputation_api
import schemas.transaction_status_api.response_schemas as transaction_status_api
import schemas.wallet_bridge_api.response_schemas as wallet_bridge_api
from schemas.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from types import ModuleType
    from typing import Final


def prepare_list_of_types() -> list[tuple[str, type[PreconfiguredBaseModel]]]:
    apis: Final[list[tuple[str, ModuleType]]] = [
        ("account_by_key_api", account_by_key_api),
        ("account_history_api", account_history_api),
        ("block_api", block_api),
        ("condenser_api", condenser_api),
        ("database_api", database_api),
        ("debug_node_api", debug_node_api),
        ("jsonrpc", jsonrpc),
        ("market_history_api", market_history_api),
        ("network_broadcast_api", network_broadcast_api),
        ("network_node_api", network_node_api),
        ("rc_api", rc_api),
        ("reputation_api", reputation_api),
        ("transaction_status_api", transaction_status_api),
        ("wallet_bridge_api", wallet_bridge_api),
    ]
    result: list[tuple[str, type[PreconfiguredBaseModel]]] = []
    for api_name, api in apis:
        for value in list(api.__dict__.values()):
            if hasattr(value, "as_strict_model"):
                result.append((f"{api_name}.{value.__name__}", value))
    return result


@pytest.mark.parametrize("model_name, model", prepare_list_of_types())
def test_smoke_as_strict_model(model_name: str, model: type[PreconfiguredBaseModel]) -> None:
    assert model.as_strict_model() is not None, model_name
