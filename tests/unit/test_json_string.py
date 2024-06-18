from __future__ import annotations

import json
from typing import Final

from schemas.operations.custom_json_operation import CustomJsonOperation

JSON_STRING_LEVEL3: Final[str] = '"c"'
JSON_STRING_LEVEL2: Final[str] = '{"b": ' + JSON_STRING_LEVEL3 + "}"
JSON_STRING_LEVEL1: Final[str] = '{"a": ' + JSON_STRING_LEVEL2 + "}"
FOLLOW_OPERATION_JSON_STRING: Final[str] = '["follow",{"follower":"abs","following":"xyz","what":["blog"]}]'
NUMBER_STRING: Final[str] = "123"
CUSTOM_JSON_ID: Final[str] = "my_id"


def test_json_getter_outer() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)

    # ACT
    json_root = op.json_.value

    # ASSERT
    assert json_root == json.loads(JSON_STRING_LEVEL1)


def test_json_getter() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)

    # ACT
    assert isinstance(op.json_.value, dict)
    a = op.json_.value["a"]

    # ASSERT
    assert a == json.loads(JSON_STRING_LEVEL2)


def test_json_getter_inner() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)

    # ACT
    assert isinstance(op.json_.value, dict)
    assert isinstance(op.json_.value["a"], dict)
    b = op.json_.value["a"]["b"]

    # ASSERT
    assert b == json.loads(JSON_STRING_LEVEL3)


def test_json_setter_outer() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)
    new_value: Final[str] = "d"

    # ACT
    op.json_.value = new_value

    # ASSERT
    assert op.json_.value == new_value


def test_json_setter() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)
    new_value: Final[str] = "e"

    # ACT
    assert isinstance(op.json_.value, dict)
    op.json_.value["a"] = new_value

    # ASSERT
    assert op.json_.value["a"] == new_value


def test_json_setter_inner() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)
    new_value: Final[str] = "f"

    # ACT
    assert isinstance(op.json_.value, dict)
    assert isinstance(op.json_.value["a"], dict)
    op.json_.value["a"]["b"] = new_value

    # ASSERT
    assert op.json_.value["a"]["b"] == new_value


def test_json_update() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=NUMBER_STRING)
    update_with: Final[dict[str, str]] = {"x": "y", "z": "t"}

    # ACT
    op.json_.value = {}
    op.json_.value.update(update_with)

    # ASSERT
    assert op.json_.value == update_with


def test_json_update_by_getattr() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=NUMBER_STRING)
    update_with: Final[dict[str, str]] = {"x": "y", "z": "t"}

    # ACT
    op.json_.value = {}
    op.json_.update(update_with)

    # ASSERT
    assert op.json_.value == update_with


def test_json_extend() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=NUMBER_STRING)
    extend_with: Final[list[str]] = ["m", "n", "p"]

    # ACT
    op.json_.value = []
    op.json_.value.extend(extend_with)

    # ASSERT
    assert op.json_.value == extend_with


def test_json_extend_by_getattr() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=NUMBER_STRING)
    extend_with: Final[list[str]] = ["m", "n", "p"]

    # ACT
    op.json_.value = []
    op.json_.extend(extend_with)

    # ASSERT
    assert op.json_.value == extend_with


def test_dumps() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=FOLLOW_OPERATION_JSON_STRING
    )

    # ACT
    dumps = op.json_.as_string
    json_value = json.loads(FOLLOW_OPERATION_JSON_STRING)
    minimal_json_string = json.dumps(json_value, separators=(",", ":"))

    # ASSERT
    assert dumps == minimal_json_string


def test_set_value() -> None:
    # ARRANGE
    int_value: Final[int] = 123
    op = CustomJsonOperation(
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=FOLLOW_OPERATION_JSON_STRING
    )

    # ACT
    op.json_.value = int_value
    serialized = json.dumps(int_value)

    # ASSERT
    assert op.json_.as_string == serialized


def test_get_by_subscript() -> None:
    # ARRANGE
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)

    # ACT
    actual_value = op.json_["a"]
    expected_value = json.loads(JSON_STRING_LEVEL2)

    # ASSERT
    assert actual_value == expected_value


def test_set_by_subscript() -> None:
    # ARRANGE
    int_value: Final[int] = 124
    op = CustomJsonOperation(required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JSON_STRING_LEVEL1)

    # ACT
    op.json_["a"] = int_value
    actual_value = op.json_["a"]
    expected_value = int_value

    # ASSERT
    assert actual_value == expected_value
