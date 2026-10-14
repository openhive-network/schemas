from __future__ import annotations

import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.errors import ValidationError
from schemas.fields.assets import AssetHive, LegacyAssetHive
from schemas.fields.basic import AccountName
from schemas.fields.hive_int import HiveInt
from schemas.validation import SchemaError, is_matching_model, validate, validate_schema_field


class Account(PreconfiguredBaseModel, kw_only=True):
    name: AccountName
    balance: AssetHive
    post_count: HiveInt
    memo: str | None = None


class LegacyAccount(PreconfiguredBaseModel, kw_only=True):
    name: AccountName
    balance: LegacyAssetHive


class GetAccountsResponse(PreconfiguredBaseModel, kw_only=True):
    accounts: list[Account]


def nai_hive(amount: str = "1000") -> dict[str, object]:
    return {"amount": amount, "precision": 3, "nai": "@@000000021"}


def account(**overrides: object) -> dict[str, object]:
    return {"name": "alice", "balance": nai_hive(), "post_count": 3, **overrides}


def test_valid_data_has_no_errors() -> None:
    # ACT
    errors = validate({"accounts": [account()]}, GetAccountsResponse)

    # ASSERT
    assert errors == []


def test_all_errors_are_collected_with_paths() -> None:
    # ARRANGE
    data = {
        "accounts": [
            account(name="Invalid!"),
            account(balance={"amount": "1", "precision": 3, "nai": "@@000000013"}),
            {"name": "bob", "balance": nai_hive()},
        ]
    }

    # ACT
    errors = validate(data, GetAccountsResponse)

    # ASSERT
    paths = {error.path for error in errors}
    assert paths == {"$.accounts[0].name", "$.accounts[1].balance", "$.accounts[2]"}, errors
    assert SchemaError("$.accounts[2]", "Object missing required field `post_count`") in errors


def test_unknown_field_is_reported() -> None:
    # ACT
    errors = validate({"accounts": [account(new_field=1)]}, GetAccountsResponse)

    # ASSERT
    assert errors == [SchemaError("$.accounts[0].new_field", "Object contains unknown field `new_field`")]


def test_errors_in_dict_values_have_paths() -> None:
    # ACT
    errors = validate({"alice": account(name="Invalid!")}, dict[str, Account])

    # ASSERT
    assert [error.path for error in errors] == ["$.alice.name"]


@pytest.mark.parametrize(
    ("model", "valid_balance", "balance_in_other_form"),
    [(Account, nai_hive(), "1.000 HIVE"), (LegacyAccount, "1.000 HIVE", nai_hive())],
)
def test_assets_are_validated_in_form_given_by_their_type(
    model: type[PreconfiguredBaseModel], valid_balance: object, balance_in_other_form: object
) -> None:
    # ARRANGE
    data = {"name": "alice", "balance": valid_balance, "post_count": 3}
    if model is LegacyAccount:
        del data["post_count"]

    # ACT & ASSERT
    assert validate(data, model) == []
    assert [error.path for error in validate({**data, "balance": balance_in_other_form}, model)] == ["$.balance"]


def test_custom_model_validates_only_its_fields() -> None:
    # ARRANGE
    class OnlyName(PreconfiguredBaseModel, forbid_unknown_fields=False):
        name: AccountName

    data = [account(post_count="not a number")]

    # ACT & ASSERT
    assert validate(data, list[OnlyName]) == []
    assert validate(data, list[Account]) != []


@pytest.mark.parametrize(("value", "matches"), [("alice", True), ("Invalid!", False), (5, False)])
def test_is_matching_model(value: object, *, matches: bool) -> None:
    # ACT & ASSERT
    assert is_matching_model(value, AccountName) is matches


def test_validate_schema_field() -> None:
    # ACT & ASSERT
    assert validate_schema_field("alice", AccountName) == "alice"
    with pytest.raises(ValidationError):
        validate_schema_field("Invalid!", AccountName)
