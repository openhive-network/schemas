from __future__ import annotations

from typing import Any

import pytest
from pydantic import BaseModel

from schemas.__private.hive_fields_schemas import EmptyString, HiveInt
from schemas.operations import AccountWitnessProxyOperation


@pytest.mark.parametrize("hive_int", [1, "312412", 412441])
def test_hive_int_with_correct_values(hive_int: int | str) -> None:
    # ARRANGE
    class TestHiveInt(BaseModel):
        example_field: HiveInt

    # ACT
    try:
        test_instance = TestHiveInt(example_field=hive_int)
    except ValueError as error:
        raise AssertionError() from error

    # ASSERT
    assert type(test_instance.example_field) is int


@pytest.mark.parametrize("not_hive_int", [True, "it is not int", 412441.412411])
def test_hive_int_with_incorrect_values(not_hive_int: Any) -> None:
    # ARRANGE
    class TestHiveInt(BaseModel):
        example_field: HiveInt

    # ACT
    try:
        TestHiveInt(example_field=not_hive_int)
    except ValueError as e:
        error = str(e)

    # ASSERT
    assert "The value could only be int or string that can be converted to int!" in error


def test_empty_string_incorrect_value() -> None:
    # ARRANGE
    class TestEmptyString(BaseModel):
        empty_str_test: EmptyString

    # ACT
    try:
        TestEmptyString(empty_str_test="it is not empty")
    except ValueError as e:
        error = str(e)

    # ASSERT
    assert "ensure this value has at most 0 characters " in error


@pytest.mark.parametrize("invalid_name", ["definitely too long name", "to", "123"])
def test_account_name_incorrect_value(invalid_name: str) -> None:
    # ARRANGE & ACT
    try:
        AccountWitnessProxyOperation(account=invalid_name, proxy=invalid_name)
    except ValueError as e:
        error = str(e)

    # ASSERT
    assert (
        "ensure this value has at most 16 characters" in error
        or "ensure this value has at least 3 characters" in error
        or "string does not match regex" in error
    )
