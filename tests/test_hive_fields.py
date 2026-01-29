from __future__ import annotations

import datetime
from typing import Any, Final, cast

import msgspec
import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.decoders import get_hf26_decoder, get_legacy_decoder
from schemas.encoders import get_hf26_encoder
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetNaiAmount, AssetVests
from schemas.fields.basic import (
    AccountName,
    EmptyString,
    PublicKey,
)
from schemas.fields.compound import Authority, HbdExchangeRate
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.hive_constants import HIVE_TIME_FORMAT

from .hive_tests_constants import ACTIVE, OWNER, POSTING


class HiveIntModel(msgspec.Struct):
    field: HiveInt


class EmptyStringModel(msgspec.Struct):
    field: EmptyString


class AccountNameModel(msgspec.Struct):
    field: AccountName


class HiveDateTimeModel(msgspec.Struct):
    field: HiveDateTime


class AuthorityModel(PreconfiguredBaseModel):
    field: Authority


class PublicKeyModel(msgspec.Struct):
    field: PublicKey


class HbdExchangeRateModelLegacy(msgspec.Struct):
    field: HbdExchangeRate


class HbdExchangeRateModelNai(msgspec.Struct):
    field: HbdExchangeRate


class AssetHiveLegacyModel(msgspec.Struct):
    field: AssetHive


@pytest.mark.parametrize("value", [1, "312412", 412441])
def test_hive_int_with_correct_values(value: int | str) -> None:
    # ACT
    instance = HiveIntModel(field=HiveInt(value))

    # ASSERT
    assert instance.field == int(value)


@pytest.mark.parametrize("value", [True, "it is not int", 412441.412411])
def test_hive_int_with_incorrect_values(value: Any) -> None:
    # ARRANGE
    expected_message: Final[str] = "The value could only be int or string that can be converted to int!"

    # ACT
    with pytest.raises(Exception) as error:
        HiveIntModel(field=HiveInt(value))

    # ASSERT
    assert expected_message in str(error.value)


def test_empty_string_correct_value() -> None:
    # ARRANGE
    instance = EmptyStringModel(field="")
    empty_string = msgspec.json.encode(instance)

    # ACT
    msgspec.json.decode(empty_string, type=EmptyStringModel)

    # ASSERT
    assert instance.field == ""  # - we want to check if it is empty string explicitly


def test_empty_string_incorrect_value() -> None:
    expected_message: Final[str] = "Expected `str` of length <= 0 - at `$.field"

    # ACT
    empty_string = msgspec.json.encode(EmptyStringModel(field="not empty"))
    with pytest.raises(msgspec.ValidationError) as error:
        msgspec.json.decode(empty_string, type=EmptyStringModel)
    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize(
    "value, expected_message",
    [
        ("definitely too long name", "Expected `str` of length <= 16"),
        ("to", "Expected `str` of length >= 3"),
        (
            "123",
            "Expected `str` matching regex '^[a-z]{1}[a-z0-9\\\\-]+[a-z0-9]{1}(:?\\\\.{1}[a-z]{1}[a-z0-9\\\\-]+[a-z0-9]{1})*$'",
        ),
    ],
)
def test_account_name_incorrect_value(value: str, expected_message: str) -> None:
    # ACT
    account_name = msgspec.json.encode(AccountNameModel(field=value))

    with pytest.raises(Exception) as error:
        get_hf26_decoder(AccountNameModel).decode(account_name)

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
    with pytest.raises(Exception) as error:
        AssetHive(amount=AssetNaiAmount(12), precision=HiveInt(3), nai=value)  # type: ignore[arg-type]

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", ["nai_pattern", "@@0000013"])
def test_asset_nai_hbd_field_incorrect_precision(value: str | int) -> None:
    # ARRANGE
    expected_message: Final[str] = "invalid literal for int() with base 10:"

    # ACT
    with pytest.raises(Exception) as error:
        AssetHbd(amount=AssetNaiAmount(10), precision=value, nai="@@000000013")  # type: ignore[arg-type]

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", ["nai_pattern", "@@0000013"])
def test_asset_nai_vests_field_incorrect_amount(value: str) -> None:
    # ARRANGE
    expected_message: Final[str] = "The value could only be int or string that can be converted to int!"

    # ACT
    with pytest.raises(Exception) as error:
        AssetVests(amount=HiveInt(value), precision=6, nai="@@000000037")

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value, valid", [("1970-01-01T00:00:00", datetime.datetime.fromtimestamp(0, tz=datetime.UTC))])
def test_hive_datetime_field_correct_values(value: str, valid: datetime.datetime) -> None:
    # ARRANGE & ACT
    instance = HiveDateTimeModel(field=HiveDateTime(value))

    # ASSERT
    assert valid == instance.field


@pytest.mark.parametrize("value", ["1970-01-01"])
def test_hive_datetime_field_incorrect_values(value: str | datetime.datetime) -> None:
    # ARRANGE
    expected_message: Final[str] = f"Date must be in format {HIVE_TIME_FORMAT}"

    # ACT
    with pytest.raises(Exception) as error:
        HiveDateTimeModel(field=HiveDateTime(value))

    # ASSERT
    assert expected_message in str(error.value)


@pytest.mark.parametrize("value", [POSTING, ACTIVE, OWNER])
def test_authority_field_correct_values(value: dict[str, Any]) -> None:
    # ACT
    instance = AuthorityModel(field=Authority(**value))

    # ASSERT
    assert instance.field.key_auths[0][0] == value["key_auths"][0][0]


@pytest.mark.parametrize(
    "authority, parameter, message",
    [
        (
            POSTING,
            "Not_int",
            "The value could only be int or string that can be converted to int!",
        ),
        (
            OWNER,
            "Bad_account_name",
            "Expected `str` matching regex '^[a-z]{1}[a-z0-9\\\\-]+[a-z0-9]{1}(:?\\\\.{1}[a-z]{1}[a-z0-9\\\\-]+[a-z0-9]{1})*$'",
        ),
        (
            ACTIVE,
            "SMT@@",
            "Expected `str` matching regex '^(?:STM)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$'",
        ),
    ],
)
def test_authority_field_incorrect_values(authority: dict[str, Any], parameter: str, message: str) -> None:
    # ARRANGE
    if authority == POSTING:
        authority["weight_threshold"] = parameter
        with pytest.raises(msgspec.ValidationError) as error:
            Authority(**authority)
        assert message in str(error.value)
        return

    if authority == OWNER:
        authority["account_auths"].append([parameter, 1])
    else:
        authority["key_auths"][0][0] = parameter
    instance = AuthorityModel(field=Authority(**authority))

    encoder = get_hf26_encoder()
    encoded_authority = encoder.encode(instance)

    decoder = get_hf26_decoder(AuthorityModel)
    # ACT
    with pytest.raises(msgspec.ValidationError) as error:
        decoder.decode(encoded_authority)

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
    expected_message: Final[str] = (
        "Expected `str` matching regex '^(?:STM)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$'"
    )

    instance = PublicKeyModel(field=value)
    public_key_model = msgspec.json.encode(instance)

    decoder = get_hf26_decoder(PublicKeyModel)
    # ACT
    with pytest.raises(Exception) as error:
        decoder.decode(public_key_model)

    # ASSERT
    assert expected_message in str(error.value)


def test_correct_value_asset_hive_legacy() -> None:
    # ACT
    hive_amount = 1000
    instance = AssetHiveLegacyModel(field="1.000 HIVE")  # type: ignore[arg-type]
    asset_hive_legacy_model = msgspec.json.encode(instance)

    decoder = get_legacy_decoder(AssetHiveLegacyModel)

    # ACT
    decoded = cast(AssetHiveLegacyModel, decoder.decode(asset_hive_legacy_model))

    # ASSERT
    assert isinstance(decoded.field, AssetHive) and decoded.field == hive_amount


def test_incorrect_value_asset_hive_legacy() -> None:
    # ARRANGE
    expected_message: Final[str] = "Given legacy asset does not match regex - at `$.field"

    instance = AssetHiveLegacyModel(field="1.000 BAD")  # type: ignore[arg-type]
    asset_hive_legacy_model = msgspec.json.encode(instance)

    decoder = get_legacy_decoder(AssetHiveLegacyModel)

    # ACT
    with pytest.raises(Exception) as error:
        decoder.decode(asset_hive_legacy_model)

    # ASSERT
    assert expected_message in str(error.value)
