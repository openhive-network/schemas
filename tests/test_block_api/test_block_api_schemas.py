from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.block_api.response_schemas import GetBlock, GetBlockHeader, GetBlockRange
from schemas.jsonrpc import get_response_model

from .resonse_schemas import GET_BLOCK, GET_BLOCK_HEADER, GET_BLOCK_RANGE


@pytest.mark.parametrize(
    "schema, parameters, endpoint",
    [
        (GetBlock, GET_BLOCK, "block_api.get_block"),
        (GetBlockHeader, GET_BLOCK_HEADER, "block_api.get_block_header"),
        (GetBlockRange, GET_BLOCK_RANGE, "block_api.get_block_range"),
    ],
)
def test_block_api_schemas_correct_values(schema: Any, parameters: dict[str, Any], endpoint: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, endpoint, **parameters)
