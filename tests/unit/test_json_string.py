from __future__ import annotations

import json
from typing import Any, Final

import pytest
from msgspec import field

from schemas.application_operation import ApplicationOperation
from schemas.decoders import get_hf26_decoder
from schemas.encoders import get_hf26_encoder
from schemas.fields.basic import AccountName
from schemas.fields.resolvables import JsonString
from schemas.operations.custom_json_operation import CustomJsonOperation, CustomJsonOperationGeneric

JSON_STRING_LEVEL3: Final[str] = '"c"'
JSON_STRING_LEVEL2: Final[str] = '{"b": ' + JSON_STRING_LEVEL3 + "}"
JSON_STRING_LEVEL1: Final[str] = '{"a": ' + JSON_STRING_LEVEL2 + "}"
FOLLOW_OPERATION_JSON_STRING: Final[str] = '["follow",{"follower":"abs","following":"xyz","what":["blog"]}]'
NUMBER_STRING: Final[str] = "123"
CUSTOM_JSON_ID: Final[str] = "my_id"

SERIALIZED_OPERATION: Final[str] = r'{"from":"abc","to":"xyz","what":["topic"]}'
JSON_OPERATION_STRING: Final[str] = (
    r'{"required_auths": [], "required_posting_auths": [], "id": "my_id", "json": "'
    + SERIALIZED_OPERATION.replace('"', r"\"")
    + r'"}'
)
SERIALIZED_JSON_STRING: Final[str] = json.dumps(json.loads(JSON_OPERATION_STRING), sort_keys=True)

JSON_STRING_INVALID_TYPE_PATTERN: Final[str] = "is not a valid type"


class ApplicationTestOperation(ApplicationOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    what: list[str]

    @classmethod
    def get_name(cls) -> str:
        return "aplication_test"


class SomeCustomType(ApplicationOperation):
    @classmethod
    def get_name(cls) -> str:
        return "some_custom_type"


class InvalidCustomType:
    pass


def make_full_model(object_: Any) -> Any:
    decoder = get_hf26_decoder(type(object_))
    encoder = get_hf26_encoder()
    encoded = encoder.encode(object_)
    return decoder.decode(encoded)


def test_json_getter_outer() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    json_root = op.json_.value

    # ASSERT
    assert json_root == json.loads(JSON_STRING_LEVEL1)


def test_json_getter() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    assert isinstance(op.json_.value, dict)
    a = op.json_.value["a"]

    # ASSERT
    assert a == json.loads(JSON_STRING_LEVEL2)


def test_json_getter_inner() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    assert isinstance(op.json_.value, dict)
    assert isinstance(op.json_.value["a"], dict)
    b = op.json_.value["a"]["b"]

    # ASSERT
    assert b == json.loads(JSON_STRING_LEVEL3)


@pytest.mark.parametrize("new_value", [123, "abc", ["a", "b", "c"], {"a": 1, "b": 2, "c": 3}])
def test_json_setter_outer(new_value: Any) -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    op.json_.value = new_value

    # ASSERT
    assert op.json_.value == new_value


def test_json_setter() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    new_value: Final[str] = "e"

    # ACT
    assert isinstance(op.json_.value, dict)
    op.json_.value["a"] = new_value

    # ASSERT
    assert op.json_.value["a"] == new_value


def test_json_setter_inner() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    new_value: Final[str] = "f"

    # ACT
    assert isinstance(op.json_.value, dict)
    assert isinstance(op.json_.value["a"], dict)
    op.json_.value["a"]["b"] = new_value

    # ASSERT
    assert op.json_.value["a"]["b"] == new_value


def test_json_update() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JsonString.resolve(type, NUMBER_STRING)
    )
    update_with: Final[dict[str, str]] = {"x": "y", "z": "t"}

    # ACT
    op.json_.value = {}
    op.json_.value.update(update_with)

    # ASSERT

    # ASSERT
    assert op.json_.value == update_with


def test_json_extend() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JsonString.resolve(type, NUMBER_STRING)
    )
    extend_with: Final[list[str]] = ["m", "n", "p"]

    # ACT
    op.json_.value = []
    op.json_.value.extend(extend_with)

    # ASSERT
    assert op.json_.value == extend_with


def test_serialization() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, FOLLOW_OPERATION_JSON_STRING),
    )

    # ACT
    dumps = op.json_.serialize()
    json_value = json.loads(FOLLOW_OPERATION_JSON_STRING)
    minimal_json_string = json.dumps(json_value, separators=(",", ":"))

    # ASSERT
    assert dumps == minimal_json_string


def test_get_by_subscript() -> None:
    # ARRANGE
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    actual_value = op.json_["a"]
    expected_value = json.loads(JSON_STRING_LEVEL2)

    # ASSERT
    assert actual_value == expected_value


def test_set_by_subscript() -> None:
    # ARRANGE
    int_value: Final[int] = 124
    op = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    op.json_["a"] = int_value
    actual_value = op.json_["a"]
    expected_value = int_value

    # ASSERT
    assert actual_value == expected_value


def test_construct_from_int() -> None:
    # ARRANGE
    some_int: Final[int] = 125
    op = CustomJsonOperation(
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=JsonString.resolve(type, some_int)
    )

    update_with: Final[dict[str, str]] = {"x": "y", "z": "t"}

    # ACT
    op.json_.value = {}
    op.json_.value.update(update_with)

    # ASSERT
    assert op.json_.value == update_with


def test_application_operation_serialize() -> None:
    # ARRANGE
    example_operation = ApplicationTestOperation(from_="abc", to="xyz", what=["topic"])
    json_string = JsonString[ApplicationTestOperation].resolve(type, example_operation)

    # ACT
    # ASSERT
    assert json_string.serialize() == SERIALIZED_OPERATION


def test_json_string_with_application_operation_serialize() -> None:
    # ARRANGE
    example_operation = ApplicationTestOperation(from_="abc", to="xyz", what=["topic"])

    # ACT
    op = CustomJsonOperationGeneric(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, example_operation),
    )

    # ASSERT
    assert op.json(order="sorted") == SERIALIZED_JSON_STRING


def test_application_operation_parse() -> None:
    # ARRANGE
    # ACT
    json_string = JsonString.resolve(type, SERIALIZED_OPERATION)  # type: ignore[var-annotated]

    # ASSERT
    assert json_string.serialize() == SERIALIZED_OPERATION


def test_json_string_with_application_operation_parse() -> None:
    # ARRANGE
    # ACT
    op = CustomJsonOperation.parse_raw(SERIALIZED_JSON_STRING, get_hf26_decoder)

    # ASSERT
    assert op.json(order="sorted") == SERIALIZED_JSON_STRING


def test_json_string_with_custom_type() -> None:
    # ACT
    # ASSERT
    JsonString(SomeCustomType())


def test_negative_json_string_with_custom_type() -> None:
    # ACT
    # ASSERT
    with pytest.raises(ValueError, match=JSON_STRING_INVALID_TYPE_PATTERN):
        JsonString.resolve(type, InvalidCustomType())


def test_application_operation_validate_from_string() -> None:
    # ACT
    # ASSERT
    ApplicationTestOperation.validate(SERIALIZED_OPERATION)


def test_application_operation_validate_from_copy() -> None:
    # ARRANGE
    application_operation = ApplicationTestOperation.validate(SERIALIZED_OPERATION)

    # ACT
    # ASSERT
    ApplicationTestOperation.validate(application_operation)


def test_negative_application_operation_validate_from_string_incorrect() -> None:
    # ARRANGE
    prepared_operation_string_incorrect = SERIALIZED_OPERATION + "abc"
    error_pattern = "is not a valid application operation string"

    # ACT
    # ASSERT
    with pytest.raises(ValueError, match=error_pattern):
        ApplicationTestOperation.validate(prepared_operation_string_incorrect)


def test_negative_application_operation_validate_any_incorrect() -> None:
    # ARRANGE
    incorrect_type_instance = InvalidCustomType()
    error_pattern = "is not a valid type"

    # ACT
    # ASSERT
    with pytest.raises(ValueError, match=error_pattern):
        ApplicationTestOperation.validate(incorrect_type_instance)


def test_negative_custom_json_operation_with_invalid_application_operation() -> None:
    # ARRANGE
    error_pattern = "is not a valid type"

    # ACT
    # ASSERT
    with pytest.raises(ValueError, match=error_pattern):
        CustomJsonOperationGeneric(
            required_auths=[],
            required_posting_auths=[],
            id_=CUSTOM_JSON_ID,
            json_=JsonString.resolve(type, InvalidCustomType()),
        )


def test_negative_custom_json_operation_with_invalid_json_string() -> None:
    # ARRANGE
    error_pattern = "is not a valid type"

    # ACT
    # ASSERT
    with pytest.raises(ValueError, match=error_pattern):
        CustomJsonOperationGeneric(
            required_auths=[],
            required_posting_auths=[],
            id_=CUSTOM_JSON_ID,
            json_=JsonString.resolve(type, JsonString(InvalidCustomType())),
        )


def test_comparison_new_object() -> None:
    # ARRANGE
    op1 = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )

    # ACT
    # ASSERT
    op2 = CustomJsonOperation(
        required_auths=[],
        required_posting_auths=[],
        id_=CUSTOM_JSON_ID,
        json_=JsonString.resolve(type, JSON_STRING_LEVEL1),
    )
    assert op1 == op2
