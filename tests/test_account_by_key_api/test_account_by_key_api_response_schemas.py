from __future__ import annotations

import json
from typing import Any

import msgspec
import pytest

from schemas.apis.account_by_key_api.response_schemas import GetKeyReferences
from schemas.encoders import enc_hook_hf26
from schemas.jsonrpc import get_response_model

from .response_from_api import GET_KEY_REFERENCES


@pytest.mark.parametrize("schema, parameters", [(GetKeyReferences, GET_KEY_REFERENCES)])
def test_response_schema_correct_value(schema: Any, parameters: dict[str, Any]) -> None:
    encoder = msgspec.json.Encoder(enc_hook=enc_hook_hf26, order="sorted")
    # ARRANGE
    pattern = json.dumps(parameters, sort_keys=True, separators=(",", ":"))

    # ACT
    parsed = get_response_model(schema, json.dumps(parameters), "hf26")
    reserialized = encoder.encode(parsed).decode()

    # ASSERT
    assert pattern == reserialized
