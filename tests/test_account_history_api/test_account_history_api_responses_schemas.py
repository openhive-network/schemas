from __future__ import annotations

import json
from typing import Any

import pytest

from schemas.apis.account_history_api.response_schemas import (
    EnumVirtualOps,
    GetAccountHistory,
    GetOpsInBlock,
    GetTransaction,
)
from schemas.jsonrpc import get_response_model
from schemas.jsonrpc_constants import JSONRPCBase, JSONRPCError

from .responses_from_api import (
    ENUM_VIRTUAL_OPS,
    GET_ACCOUNT_HISTORY,
    GET_OPS_IN_BLOCK,
    GET_TRANSACTION,
)


@pytest.mark.parametrize(
    "schema, parameters, endpoint",
    [
        (EnumVirtualOps, ENUM_VIRTUAL_OPS, "account_history_api.enum_virtual_ops"),
        (GetAccountHistory, GET_ACCOUNT_HISTORY, "account_history_api.get_account_history"),
        (GetOpsInBlock, GET_OPS_IN_BLOCK, "account_history_api.get_ops_in_block"),
        (GetTransaction, GET_TRANSACTION, "account_history_api.get_transaction"),
    ],
)
def test_account_history_api_correct_values(parameters: dict[str, Any], schema: Any, endpoint: Any) -> None:
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True)

    # ACT
    parsed: JSONRPCBase | JSONRPCError = get_response_model(schema, endpoint, **parameters)
    reserialized = parsed.json(by_alias=True, sort_keys=True)

    # ASSERT
    assert pattern == reserialized
