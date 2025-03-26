from __future__ import annotations

import json
from typing import Any

import msgspec
import pytest

from schemas.apis.account_history_api.response_schemas import (
    EnumVirtualOps,
    GetAccountHistory,
    GetOpsInBlock,
    GetTransaction,
)
from schemas.encoders import enc_hook_hf26
from schemas.jsonrpc import get_response_model

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
    encoder = msgspec.json.Encoder(enc_hook=enc_hook_hf26, order="sorted")
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True, separators=(",", ":"))

    # ACT
    parsed = get_response_model(schema, json.dumps(parameters), "hf26")
    reserialized = encoder.encode(parsed).decode()

    # ASSERT
    assert pattern == reserialized
