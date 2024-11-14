from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.transaction_status_api.response_schemas import FindTransaction
from schemas.jsonrpc import get_response_model

from .response_schemas import FIND_TRANSACTION


@pytest.mark.parametrize(
    "schema, parameters, endpoint", [(FindTransaction, FIND_TRANSACTION, "transaction_status_api.find_transaction")]
)
def test_transaction_status_api_correct_values(schema: Any, parameters: dict[str, Any], endpoint: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, endpoint, **parameters)
