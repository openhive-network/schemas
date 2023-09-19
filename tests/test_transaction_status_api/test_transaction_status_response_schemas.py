from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.transaction_status_api.response_schemas import FindTransaction
from schemas.jsonrpc import get_response_model

from .response_schemas import FIND_TRANSACTION


@pytest.mark.parametrize("schema, parameters", [(FindTransaction, FIND_TRANSACTION)])
def test_transaction_status_api_correct_values(schema: Any, parameters: dict[str, Any]) -> None:
    # ACT & ASSERT
    get_response_model(schema, **parameters)
