from __future__ import annotations

from typing import Any

import pytest

from schemas.__private.hive_factory import HiveResult
from schemas.transaction_status_api.response_schemas import FindTransaction

from .response_schemas import FIND_TRANSACTION


@pytest.mark.parametrize("schema, parameters", [(FindTransaction, FIND_TRANSACTION)])
def test_transaction_status_api_correct_values(schema: Any, parameters: dict[str, Any]) -> None:
    # ACT & ASSERT
    HiveResult.factory(schema, **parameters)
