from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.account_by_key_api.response_schemas import GetKeyReferences
from schemas.jsonrpc import get_response_model

from .response_from_api import GET_KEY_REFERENCES


@pytest.mark.parametrize(
    "schema, parameters, endpoint", [(GetKeyReferences, GET_KEY_REFERENCES, "account_by_key_api.get_key_references")]
)
def test_response_schema_correct_value(schema: Any, parameters: dict[str, Any], endpoint: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, endpoint, **parameters)
