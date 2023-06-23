from __future__ import annotations

import json
from typing import Any

import pytest

from schemas.__private.hive_factory import HiveError, HiveResult
from schemas.__private.operation_objects import Hf26ApiOperationObject, Hf26ApiVirtualOperationObject
from schemas.__private.operations import Hf26OperationRepresentationType
from schemas.account_history_api.response_schemas import (
    EnumVirtualOpsModel,
    GetAccountHistoryModel,
    GetOpsInBlockModel,
    GetTransactionModel,
)
from .responses_from_api import (
    ENUM_VIRTUAL_OPS,
    GET_ACCOUNT_HISTORY,
    GET_OPS_IN_BLOCK,
    GET_TRANSACTION,
)


@pytest.mark.parametrize(
    "schema, parameters",
    [
        (EnumVirtualOpsModel[Hf26ApiVirtualOperationObject], ENUM_VIRTUAL_OPS),
        (GetAccountHistoryModel[Hf26ApiOperationObject, Hf26ApiVirtualOperationObject], GET_ACCOUNT_HISTORY),
        (GetOpsInBlockModel[Hf26ApiOperationObject, Hf26ApiVirtualOperationObject], GET_OPS_IN_BLOCK),
        (GetTransactionModel[Hf26OperationRepresentationType], GET_TRANSACTION),
    ],
)
def test_account_history_api_correct_values(parameters: dict[str, Any], schema: Any) -> None:
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True)

    # ACT
    parsed: HiveResult[schema] | HiveError[schema] = HiveResult.factory(schema, **parameters)
    reserialized = parsed.json(by_alias=True, sort_keys=True)

    # ASSERT
    assert pattern == reserialized
