from __future__ import annotations

import datetime
from typing import Any

import pytest
from pydantic import BaseModel, ValidationError

from schemas.__private.hive_fields_schemas import EmptyString, HiveInt
from schemas.__private.hive_fields_schemas_strict import AssetHbdNaiStrict, AssetHiveNaiStrict, AssetVestsNaiStrict
from schemas.operations import AccountWitnessProxyOperation, ResetAccountOperation, UpdateProposalOperation
from tests.hive_tests_constants import ACTIVE, OWNER, POSTING


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


@pytest.mark.parametrize(
    "valid_datetime", ["1970-01-01T00:00:00", datetime.datetime.strptime("1970-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S")]
)
def test_hive_datetime_field_correct_values(valid_datetime: str | datetime.datetime) -> None:
    # ARRANGE
    reference_date = datetime.datetime.strptime("1970-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
    date_after_operation = reference_date + datetime.timedelta(days=2)

    # ACT
    try:
        test_instance = UpdateProposalOperation(
            proposal_id=123,
            creator="alice",
            daily_pay="1.000 HBD",
            subject="test_subject",
            permlink="test_permlink",
            extensions=valid_datetime,
        )
    except ValidationError as error:
        raise ValueError("Data in invalid format") from error

    test_operation_on_date = test_instance.extensions + datetime.timedelta(days=2)

    # ASSERT
    assert reference_date == test_instance.extensions and date_after_operation == test_operation_on_date


@pytest.mark.parametrize("invalid_datetime", ["1970-01-01"])
def test_hive_datetime_field_incorrect_values(invalid_datetime: str | datetime.datetime) -> None:
    # ARRANGE & ACT
    try:
        UpdateProposalOperation(
            proposal_id=123,
            creator="alice",
            daily_pay="1.000 HBD",
            subject="test_subject",
            permlink="test_permlink",
            extensions=invalid_datetime,
        )
    except ValidationError as e:
        error = str(e)

    # ASSERT
    assert "date must be in format %Y-%m-%dT%H:%M:%S" in error


@pytest.mark.parametrize("authority", [POSTING, ACTIVE, OWNER])
def test_authority_field_correct_values(authority: dict[str, Any]) -> None:
    # ARRANGE & ACT
    try:
        ResetAccountOperation(reset_account="initminer", account_to_reset="alice", new_owner_authority=authority)
    except ValidationError as error:
        raise ValueError("Error in authority field") from error


@pytest.mark.parametrize("authority, parameter", [(POSTING, "Not_int"), (OWNER, "Bad_account_name"), (ACTIVE, "SMT@@")])
def test_authority_field_incorrect_values(authority: dict[str, Any], parameter: str) -> None:
    # ARRANGE
    if authority == POSTING:
        authority["weight_threshold"] = parameter
    elif authority == OWNER:
        authority["account_auths"].append([parameter, 1])
    else:
        authority["key_auths"][0][0] = parameter

    # ACT
    try:
        ResetAccountOperation(reset_account="alice", account_to_reset="alice", new_owner_authority=authority)
    except ValidationError as e:
        error = str(e)

    # ASSERT
    assert "string does not match regex" in error or "he value could only be int" in error
