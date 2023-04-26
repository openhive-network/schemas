from __future__ import annotations

import datetime
from typing import Any, Final

import pytest
from pydantic import BaseModel, ValidationError

from schemas.__private.hive_fields_schemas import AccountName, EmptyString, HiveInt, PublicKey
from schemas.__private.hive_fields_schemas_strict import AssetHbdNaiStrict, AssetHiveNaiStrict, AssetVestsNaiStrict
from schemas.operations import ResetAccountOperation, UpdateProposalOperation

from .hive_tests_constants import ACTIVE, OWNER, POSTING


class HiveIntModel(BaseModel):
    field: HiveInt


class EmptyStringModel(BaseModel):
    field: EmptyString


class AccountNameModel(BaseModel):
    field: AccountName


@pytest.mark.parametrize("value", [1, "312412", 412441])
def test_hive_int_with_correct_values(value: int | str) -> None:
    # ACT
    instance = HiveIntModel(field=value)

    # ASSERT
    assert instance.field == int(value)


@pytest.mark.parametrize("value", [True, "it is not int", 412441.412411])
def test_hive_int_with_incorrect_values(value: Any) -> None:
    # ARRANGE
    expected_message: Final[str] = "The value could only be int or string that can be converted to int!"

    # ACT
    with pytest.raises(ValidationError) as error:
        HiveIntModel(field=value)

    # ASSERT
    assert expected_message in str(error.value)


def test_empty_string_correct_value() -> None:
    # ACT
    instance = EmptyStringModel(field="")

    # ASSERT
    assert instance.field == ""  # noqa: PLC1901 - we want to check if it is empty string explicitly


def test_empty_string_incorrect_value() -> None:
    expected_message: Final[str] = "ensure this value has at most 0 characters"

    # ACT
    with pytest.raises(ValidationError) as error:
        EmptyStringModel(field="not empty")

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize(
    "value, expected_message",
    [
        ("definitely too long name", "ensure this value has at most 16 characters"),
        ("to", "ensure this value has at least 3 characters"),
        ("123", "string does not match regex"),
    ],
)
def test_account_name_incorrect_value(value: str, expected_message: str) -> None:
    # ACT
    with pytest.raises(ValidationError) as error:
        AccountNameModel(field=value)

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", ["alice", "bob", "initminer"])
def test_account_name_correct_value(value: str) -> None:
    # ACT
    instance = AccountNameModel(field=value)

    # ASSERT
    assert instance.field == value


@pytest.mark.parametrize("value", ["incorrect", 12345, "@@0000021"])
def test_asset_nai_hive_field_incorrect_pattern(value: str | int) -> None:
    # ARRANGE
    expected_message: Final[str] = "Invalid nai !"

    # ACT
    with pytest.raises(ValidationError) as error:
        AssetHiveNaiStrict(amount=12, precision=3, nai=value)

    # ASSERT
    assert expected_message in str(error.value)


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


@pytest.mark.parametrize(
    "public_key",
    [
        "SMM69zfrFGnZtU3gWFWpQJ6GhND1nz7TJsKBTjcWfebS1JzBEweQy",
        "STM12345",
        "STM1234KASJDzskakxKqwedskldmeokllsdsdbfwsggdaWf123dfs3efa2sga2wdwsfnKSM",
    ],
)
def test_public_key_field_incorrect_values(public_key: str) -> None:
    # ARRANGE
    class TestPublicKey(BaseModel):
        test_key: PublicKey

    # ACT
    try:
        TestPublicKey(test_key=public_key)
    except ValidationError as e:
        error = str(e)

    # ASSERT
    assert "string does not match regex" in error
