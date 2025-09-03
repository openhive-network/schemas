from __future__ import annotations

from typing import Any, Final

import msgspec
import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel

FIRST_MODEL_SCHEMA_PATTERN: Final[dict[str, Any]] = {
    "$ref": "#/$defs/FirstModel",
    "$defs": {
        "FirstModel": {
            "title": "FirstModel",
            "type": "object",
            "properties": {"a": {"type": "integer"}},
            "required": ["a"],
            "additionalProperties": False,
        }
    },
}

SECOND_MODEL_SCHEMA_PATTERN: Final[dict[str, Any]] = {
    "$ref": "#/$defs/SecondModel",
    "$defs": {
        "SecondModel": {
            "title": "SecondModel",
            "type": "object",
            "properties": {"a": {"type": "integer"}, "c": {"type": "integer"}},
            "required": ["a", "c"],
            "additionalProperties": False,
        }
    },
}

THIRD_MODEL_SCHEMA_PATTERN: Final[dict[str, Any]] = {
    "$ref": "#/$defs/ThirdModel",
    "$defs": {
        "ThirdModel": {
            "title": "ThirdModel",
            "type": "object",
            "properties": {"e": {"$ref": "#/$defs/FirstModel"}, "f": {"type": "string"}},
            "required": ["e", "f"],
            "additionalProperties": False,
        },
        "FirstModel": {
            "title": "FirstModel",
            "type": "object",
            "properties": {"a": {"type": "integer"}},
            "required": ["a"],
            "additionalProperties": False,
        },
    },
}
FOURTH_MODEL_SCHEMA_PATTERN: Final[dict[str, Any]] = {
    "$ref": "#/$defs/FourthModel",
    "$defs": {
        "FourthModel": {
            "title": "FourthModel",
            "type": "object",
            "properties": {"h": {"type": "integer"}},
            "required": ["h"],
            "additionalProperties": False,
        }
    },
}


class FirstModel(PreconfiguredBaseModel):
    a: int
    b: str

    @classmethod
    def excluded_fields_for_schema_json(cls) -> set[str]:
        return {"b"}


class SecondModel(FirstModel):
    c: int
    d: str

    @classmethod
    def excluded_fields_for_schema_json(cls) -> set[str]:
        return {"d", *super().excluded_fields_for_schema_json()}


class ThirdModel(PreconfiguredBaseModel):
    e: FirstModel
    f: str


class FourthModel(PreconfiguredBaseModel):
    g: FirstModel
    h: int

    @classmethod
    def excluded_fields_for_schema_json(cls) -> set[str]:
        return {"g"}


@pytest.mark.parametrize(
    "model_cls, expected_pattern",
    [
        (FirstModel, FIRST_MODEL_SCHEMA_PATTERN),
        (SecondModel, SECOND_MODEL_SCHEMA_PATTERN),
        (ThirdModel, THIRD_MODEL_SCHEMA_PATTERN),
        (FourthModel, FOURTH_MODEL_SCHEMA_PATTERN),
    ],
)
def test_schema_json_exclude_feature(model_cls: PreconfiguredBaseModel, expected_pattern: dict[str, Any]) -> None:
    # ACT
    actual_schema_json = model_cls.schema_json()

    # ASSERT
    actual_schema = msgspec.json.decode(actual_schema_json)
    assert actual_schema == expected_pattern, f"{model_cls} schema is different from expected one"
