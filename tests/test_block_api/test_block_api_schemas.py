from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.block_api.response_schemas import GetBlock, GetBlockHeader, GetBlockRange
from schemas.responses import HiveResult

from .resonse_schemas import GET_BLOCK, GET_BLOCK_HEADER, GET_BLOCK_RANGE


@pytest.mark.parametrize(
    "schema, parameters", [(GetBlock, GET_BLOCK), (GetBlockHeader, GET_BLOCK_HEADER), (GetBlockRange, GET_BLOCK_RANGE)]
)
def test_block_api_schemas_correct_values(schema: Any, parameters: dict[str, Any]) -> None:
    # ACT & ASSERT
    HiveResult.factory(schema, **parameters)
