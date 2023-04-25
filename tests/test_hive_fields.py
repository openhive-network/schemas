from __future__ import annotations

from typing import Any

import pytest
from pydantic import BaseModel, ValidationError

from schemas.__private.hive_fields_schemas import EmptyString, HiveInt
from schemas.__private.hive_fields_schemas_strict import AssetHbdNaiStrict, AssetHiveNaiStrict, AssetVestsNaiStrict
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


@pytest.mark.parametrize("valid_name", ["alice", "bob", "initminer"])
def test_account_name_correct_value(valid_name: str) -> None:
    # ARRANGE & ACT
    try:
        test_instance = AccountWitnessProxyOperation(account=valid_name, proxy=valid_name)
    except ValueError as error:
        raise ValueError("Invalid name format") from error

    created_account = test_instance.account
    created_proxy = test_instance.account

    # ASSERT
    assert created_account == valid_name and created_proxy == valid_name


@pytest.mark.parametrize("invalid_nai_pattern", ["nai_pattern", 12345, "@@0000021"])
def test_asset_nai_hive_field_incorrect_pattern(invalid_nai_pattern: str | int) -> None:
    # ARRANGE & ACT
    try:
        AssetHiveNaiStrict(amount=12, precision=3, nai=invalid_nai_pattern)
    except ValidationError as e:
        error = str(e)

    # ASSERT
    assert "Invalid nai !" in error


@pytest.mark.parametrize("invalid_precision", ["nai_pattern", 12345, "@@0000013"])
def test_asset_nai_hbd_field_incorrect_precision(invalid_precision: str | int) -> None:
    # ARRANGE & ACT
    try:
        AssetHbdNaiStrict(amount=12, precision=invalid_precision, nai="@@000000013")
    except ValidationError as e:
        error = str(e)

    # ASSERT
    assert "Invalid precision" or "The value could only be int or string that can be converted to int!" in error


@pytest.mark.parametrize("invalid_amount", ["nai_pattern", "@@0000013"])
def test_asset_nai_vests_field_incorrect_amount(invalid_amount: str) -> None:
    # ARRANGE & ACT
    try:
        AssetVestsNaiStrict(amount=invalid_amount, precision=6, nai="@@000000037")
    except ValidationError as e:
        error = str(e)

    # ASSERT
    assert "The value could only be int or string that can be converted to int!" in error
