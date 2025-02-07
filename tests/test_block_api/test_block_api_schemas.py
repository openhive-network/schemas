from __future__ import annotations

import json
from typing import Any

import msgspec
import pytest

from schemas.apis.block_api.response_schemas import GetBlock, GetBlockHeader, GetBlockRange
from schemas.encoders import enc_hook_hf26
from schemas.jsonrpc import get_response_model

from .resonse_schemas import GET_BLOCK, GET_BLOCK_HEADER, GET_BLOCK_RANGE


@pytest.mark.parametrize(
    "schema, parameters", [(GetBlock, GET_BLOCK), (GetBlockHeader, GET_BLOCK_HEADER), (GetBlockRange, GET_BLOCK_RANGE)]
)
def test_block_api_schemas_correct_values(schema: Any, parameters: dict[str, Any]) -> None:
    encoder = msgspec.json.Encoder(enc_hook=enc_hook_hf26, order="sorted")
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True, separators=(",", ":"))

    # ACT
    parsed = get_response_model(schema, json.dumps(parameters), "hf26")
    reserialized = encoder.encode(parsed).decode()

    # ASSERT
    assert pattern == reserialized
