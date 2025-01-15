from __future__ import annotations

import json
from typing import Any

import pytest

from schemas.apis.account_by_key_api.response_schemas import GetKeyReferences
from schemas.jsonrpc import get_response_model

from .response_from_api import GET_KEY_REFERENCES


@pytest.mark.parametrize("schema, parameters", [(GetKeyReferences, GET_KEY_REFERENCES)])
def test_response_schema_correct_value(schema: Any, parameters: dict[str, Any]) -> None:
    # ACT & ASSERT
    get_response_model(schema, json.dumps(parameters), "hf26")
