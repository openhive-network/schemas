from __future__ import annotations

import copy
import json
from typing import Any, Literal

import msgspec

from schemas.encoders import enc_hook_hf26, enc_hook_legacy
from schemas.jsonrpc import get_response_model


def verify_serialization_and_deserialization(
    schema: Any, parameters: dict[str, Any], serialization_type: Literal["hf26", "legacy"]
) -> None:
    # PATTERN
    parameters_without_sigint = convert_sigints_to_int(copy.deepcopy(parameters))
    pattern = json.dumps(parameters_without_sigint, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

    # MSGSPEC TEST
    if serialization_type == "legacy":
        encoder = msgspec.json.Encoder(enc_hook=enc_hook_legacy, order="sorted")
    else:
        encoder = msgspec.json.Encoder(enc_hook=enc_hook_hf26, order="sorted")

    serialized = get_response_model(schema, json.dumps(parameters), serialization_type)
    deserialized = encoder.encode(serialized).decode()
    deserialized_json_without_sigint = convert_sigints_to_int(json.loads(deserialized))
    verified = json.dumps(deserialized_json_without_sigint, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

    # ASSERT
    assert pattern == verified, "Verified structure is not same as pattern. Serialization or deserialization goes wrong"


def convert_sigints_to_int(data: dict[str, Any] | list[Any]) -> dict[str, Any] | list[Any]:
    """Recursively convert recognized sigints (safe integers in string format) to int."""
    if isinstance(data, dict):
        return {key: convert_sigints_to_int(value) for key, value in data.items()}
    if isinstance(data, list):
        return [convert_sigints_to_int(item) for item in data]
    if isinstance(data, str) and data.isdigit():
        return int(data)
    return data
