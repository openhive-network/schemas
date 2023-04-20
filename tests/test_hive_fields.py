from __future__ import annotations

from typing import Any

import pytest
from pydantic import BaseModel

from schemas.__private.hive_fields_schemas_strict import HiveInt


@pytest.mark.parametrize("valid_value, invalid_value", [(1, True), ("312412", "xyz"), (123, 123.123)])
def test_input_different_types_to_hive_int(valid_value: Any, invalid_value: Any) -> None:
    # ARRANGE
    class TestHiveInt(BaseModel):
        example_field: HiveInt

    # ACT
    try:
        test_valid_value = TestHiveInt(example_field=valid_value)
        TestHiveInt(example_field=invalid_value)
    except ValueError as e:
        error = str(e)
    value_to_check = test_valid_value.example_field

    # ASSERT
    assert value_to_check == int(valid_value) and type(value_to_check) is int
    assert "The value could only be int or string that can be converted to int!" in error
