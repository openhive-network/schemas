from __future__ import annotations

from typing import Final

import pytest

from schemas.custom_operations.json_convertible import JsonConvertible
from schemas.operations.custom_json_operation import CustomJsonOperation

from .helpers import assert_json_contains


class UserDefinedClass(JsonConvertible):
    """User defined class must implement abstract base class schemas.fields.json_convertible.JsonConvertible"""

    a: str
    b: int


class InvalidClass:
    """Invalid class doesn't implement schemas.fields.json_convertible.JsonConvertible"""

    def __init__(self, a: str, b: int) -> None:
        self.a = a
        self.b = b


CUSTOM_JSON_ID: Final[str] = "my_id"
EXAMPLE_DATACLASS_JSON_STRING: Final[str] = '{"a": "sometextmodified", "b": 124}'


def test_dump_user_defined_class() -> None:
    # ARRANGE
    user_defined_instance = UserDefinedClass(a="sometext", b=123)

    # ACT
    op = CustomJsonOperation[UserDefinedClass](
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=user_defined_instance
    )

    # ASSERT
    assert_json_contains(user_defined_instance.json(), op.json())


def test_load_user_defined_class() -> None:
    # ACT
    op = CustomJsonOperation[UserDefinedClass](
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=EXAMPLE_DATACLASS_JSON_STRING
    )

    # ASSERT
    assert_json_contains(EXAMPLE_DATACLASS_JSON_STRING, op.json())


def test_dump_invalid_class() -> None:
    # ARRANGE
    invalid_instance = InvalidClass(a="sometext", b=123)

    # ACT
    with pytest.raises(RuntimeError, match="no validator found"):
        CustomJsonOperation[InvalidClass](  #  type: ignore[type-var]
            required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=invalid_instance
        )
