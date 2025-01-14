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
from schemas.jsonrpc import JSONRPCError, JSONRPCResult, get_response_model

from .responses_from_api import (
    ENUM_VIRTUAL_OPS,
    GET_ACCOUNT_HISTORY,
    GET_OPS_IN_BLOCK,
    GET_TRANSACTION,
)


@pytest.mark.parametrize(
    "schema, parameters",
    [
        (EnumVirtualOps, ENUM_VIRTUAL_OPS),
        (GetAccountHistory, GET_ACCOUNT_HISTORY),
        (GetOpsInBlock, GET_OPS_IN_BLOCK),
        (GetTransaction, GET_TRANSACTION),
    ],
)
def test_account_history_api_correct_values(parameters: dict[str, Any], schema: Any) -> None:
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True)

    # ACT
    parsed: JSONRPCResult[schema] | JSONRPCError = get_response_model(schema, json.dumps(parameters))
    # reserialized = parsed.json(by_alias=True, sort_keys=True)

    # # ASSERT
    # assert pattern == reserialized
