from __future__ import annotations

from typing import Any

import pytest

from schemas.__private.hive_factory import HiveResult
from schemas.account_history_api.response_schemas import (
    EnumVirtualOps,
    GetAccountHistory,
    GetOpsInBlock,
    GetTransaction,
)
from tests.test_account_history_api.responses_from_api import (
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
    # ACT & ASSERT
    HiveResult.factory(schema, **parameters)
