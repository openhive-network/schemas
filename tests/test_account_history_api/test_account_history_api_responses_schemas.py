from __future__ import annotations

import json
from typing import Any

import pytest

from schemas.__private.hive_factory import HiveResult
from schemas.account_history_api.response_schemas import (
    GetAccountHistory,
    GetOpsInBlock,
    GetTransaction,
)
from tests.test_account_history_api.responses_from_api import (
    GET_ACCOUNT_HISTORY,
    GET_OPS_IN_BLOCK,
    GET_TRANSACTION,
)


@pytest.mark.parametrize(
    "schema, parameters",
    [
        (GetAccountHistory, GET_ACCOUNT_HISTORY),
        (GetOpsInBlock, GET_OPS_IN_BLOCK),
        (GetTransaction, GET_TRANSACTION),
    ],
)
def test_account_history_api_correct_values(parameters: dict[str, Any], schema: Any) -> None:
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True)

    # ACT
    parsed: HiveResult[schema] = HiveResult.factory(schema, **parameters)
    reserialized = parsed.json(by_alias=True, sort_keys=True)

    # ASSERT
    assert pattern == reserialized
