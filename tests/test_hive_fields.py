from __future__ import annotations

import datetime
from typing import Any, Final

import pytest
from pydantic import BaseModel, ValidationError

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVestsHF26,
    Authority,
    EmptyString,
    HbdExchangeRate,
    HiveDateTime,
    HiveInt,
    PublicKey,
)

from .hive_tests_constants import ACTIVE, OWNER, POSTING


class HiveIntModel(BaseModel):
    field: HiveInt


class EmptyStringModel(BaseModel):
    field: EmptyString


class AccountNameModel(BaseModel):
    field: AccountName


class HiveDateTimeModel(BaseModel):
    field: HiveDateTime


class AuthorityModel(BaseModel):
    field: Authority


class PublicKeyModel(BaseModel):
    field: PublicKey


class HbdExchangeRateModelLegacy(BaseModel):
    field: HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy]


class HbdExchangeRateModelNai(BaseModel):
    field: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]


class AssetHiveLegacyModel(BaseModel):
    field: AssetHiveLegacy


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


@pytest.mark.parametrize("value", ["incorrect", 12345, "@@0000013"])
def test_asset_nai_hive_field_incorrect_pattern(value: str | int) -> None:
    # ARRANGE
    expected_message: Final[str] = "Invalid nai !"

    # ACT
    with pytest.raises(ValidationError) as error:
        AssetHiveHF26(amount=12, precision=3, nai=value)

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", ["nai_pattern", "@@0000013"])
def test_asset_nai_hbd_field_incorrect_precision(value: str | int) -> None:
    # ARRANGE
    expected_message: Final[str] = "The value could only be int or string that can be converted to int!"

    # ACT
    with pytest.raises(ValidationError) as error:
        AssetHbdHF26(amount=10, precision=value, nai="@@000000013")

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", ["nai_pattern", "@@0000013"])
def test_asset_nai_vests_field_incorrect_amount(value: str) -> None:
    # ARRANGE
    expected_message: Final[str] = "The value could only be int or string that can be converted to int!"

    # ACT
    with pytest.raises(ValidationError) as error:
        AssetVestsHF26(amount=value, precision=6, nai="@@000000037")

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize(
    "value, valid", [("1970-01-01T00:00:00", datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc))]
)
def test_hive_datetime_field_correct_values(value: str, valid: datetime.datetime) -> None:
    # ARRANGE & ACT
    instance = HiveDateTimeModel(field=value)

    # ASSERT
    assert valid == instance.field


@pytest.mark.parametrize("value", ["1970-01-01"])
def test_hive_datetime_field_incorrect_values(value: str | datetime.datetime) -> None:
    # ARRANGE
    expected_message: Final[str] = "date must be in format %Y-%m-%dT%H:%M:%S"

    # ACT
    with pytest.raises(ValidationError) as error:
        HiveDateTimeModel(field=value)

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", [POSTING, ACTIVE, OWNER])
def test_authority_field_correct_values(value: dict[str, Any]) -> None:
    # ACT
    instance = AuthorityModel(field=value)

    # ASSERT
    assert instance.field.key_auths[0][0] == value["key_auths"][0][0]


@pytest.mark.parametrize(
    "authority, parameter, message",
    [
        (POSTING, "Not_int", "The value could only be int or string that can be converted to int!"),
        (OWNER, "Bad_account_name", "string does not match regex"),
        (ACTIVE, "SMT@@", "string does not match regex"),
    ],
)
def test_authority_field_incorrect_values(authority: dict[str, Any], parameter: str, message: str) -> None:
    # ARRANGE
    if authority == POSTING:
        authority["weight_threshold"] = parameter
    elif authority == OWNER:
        authority["account_auths"].append([parameter, 1])
    else:
        authority["key_auths"][0][0] = parameter

    # ACT
    with pytest.raises(ValidationError) as error:
        AuthorityModel(field=authority)

    # ASSERT
    assert message in str(error.value)


@pytest.mark.parametrize(
    "value",
    [
        "SMM69zfrFGnZtU3gWFWpQJ6GhND1nz7TJsKBTjcWfebS1JzBEweQy",
        "STM12345",
        "STM1234KASJDzskakxKqwedskldmeokllsdsdbfwsggdaWf123dfs3efa2sga2wdwsfnKSM",
    ],
)
def test_public_key_field_incorrect_values(value: str) -> None:
    # ARRANGE
    expected_message: Final[str] = "string does not match regex"

    # ACT
    with pytest.raises(ValidationError) as error:
        PublicKeyModel(field=value)

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize(
    "hive_legacy, hbd_legacy, hive_nai, hbd_nai",
    [
        (
            "1.000 HIVE",
            "1.000 HBD",
            {"amount": 1, "precision": 3, "nai": "@@000000021"},
            {"amount": 1, "precision": 3, "nai": "@@000000013"},
        )
    ],
)
def test_hbd_exchange_rate_incorrect_values(
    hive_legacy: str, hbd_legacy: str, hive_nai: dict[str, Any], hbd_nai: dict[str, Any]
) -> None:
    """HbdExchangeRate accept two Asset types -> legacy and nai. Choose of the Asset type is performed by generic.
    So this test is used to check if validation after choose type of Asset is performed fine. To check it nai Assets
    have been putted to Legacy version and legacy Assets to nai version.
    """
    # ARRANGE
    expected_message_nai: Final[str] = "value is not a valid dict"
    expected_message_legacy: Final[str] = "str type expected"

    hbd_exchange_nai = HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
    hbd_exchange_legacy = HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy]

    # ACT
    with pytest.raises(ValidationError) as error_legacy:
        HbdExchangeRateModelLegacy(field=hbd_exchange_legacy(base=hbd_nai, quote=hive_nai))

    with pytest.raises(ValidationError) as error_nai:
        HbdExchangeRateModelNai(field=hbd_exchange_nai(base=hbd_legacy, quote=hive_legacy))

    # ASSERT
    assert expected_message_nai in str(error_nai.value) and expected_message_legacy in str(error_legacy.value)


def test_correct_value_asset_hive_legacy() -> None:
    # ACT
    instance = AssetHiveLegacyModel(field="1.000 HIVE")

    # ASSERT
    assert instance.field == "1.000 HIVE"


def test_incorrect_value_asset_hive_legacy() -> None:
    # ARRANGE
    expected_message: Final[str] = "string does not match regex"

    # ACT
    with pytest.raises(ValidationError) as error:
        AssetHiveLegacyModel(field="1.000 BAD")

    # ASSERT
    assert expected_message in str(error.value)
