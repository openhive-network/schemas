from __future__ import annotations

import json
import sys
import types
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.errors import ValidationError
from schemas.fields.assets import AssetHive
from schemas.fields.basic import AccountName
from schemas.fields.hive_int import HiveInt
from schemas.validation import (
    SchemaError,
    UnknownEndpointError,
    convert_to_validation_schema,
    register_validation_models,
    validate_schema,
)

if TYPE_CHECKING:
    from collections.abc import Iterator

VALIDATION_MODULE = "tests.unit._fake_validation_module"


class Account(PreconfiguredBaseModel, kw_only=True):
    name: AccountName
    balance: AssetHive
    post_count: HiveInt
    memo: str | None = None


class GetAccountsResponse(PreconfiguredBaseModel, kw_only=True):
    accounts: list[Account]


class FakeApi:
    __validation_module__ = VALIDATION_MODULE
    __serialization__ = "hf26"

    def find_accounts(self) -> None: ...


class FakeLegacyApi:
    __validation_module__ = VALIDATION_MODULE
    __serialization__ = "legacy"

    def get_accounts(self) -> None: ...


@dataclass(frozen=True, kw_only=True)
class PublicAccount:
    name: str
    balance: dict[str, Any]
    post_count: int

    def json(self) -> str:
        return json.dumps({"name": self.name, "balance": self.balance, "post_count": self.post_count})


def nai_hive(amount: str = "1000") -> dict[str, Any]:
    return {"amount": amount, "precision": 3, "nai": "@@000000021"}


def account(**overrides: Any) -> dict[str, Any]:
    return {"name": "alice", "balance": nai_hive(), "post_count": 3, **overrides}


@pytest.fixture(autouse=True)
def fake_validation_module() -> Iterator[None]:
    module = types.ModuleType(VALIDATION_MODULE)
    module.ENDPOINT_RESULTS = {  # type: ignore[attr-defined]
        "find_accounts": ("GetAccountsResponse", False),
        "get_accounts": ("Account", True),
    }
    module.Account = Account  # type: ignore[attr-defined]
    module.GetAccountsResponse = GetAccountsResponse  # type: ignore[attr-defined]
    sys.modules[VALIDATION_MODULE] = module
    register_validation_models("fake_api", VALIDATION_MODULE)
    register_validation_models("fake_legacy_api", VALIDATION_MODULE, "legacy")
    yield
    del sys.modules[VALIDATION_MODULE]


def test_valid_response_has_no_errors() -> None:
    # ACT
    errors = validate_schema({"accounts": [account()]}, "fake_api.find_accounts")

    # ASSERT
    assert errors == []


def test_all_errors_are_collected_with_paths() -> None:
    # ARRANGE
    response = {
        "accounts": [
            account(name="Invalid!"),
            account(balance={"amount": "1", "precision": 3, "nai": "@@000000013"}),
            {"name": "bob", "balance": nai_hive()},
        ]
    }

    # ACT
    errors = validate_schema(response, "fake_api.find_accounts")

    # ASSERT
    paths = {error.path for error in errors}
    assert paths == {"$.accounts[0].name", "$.accounts[1].balance", "$.accounts[2]"}, errors
    assert SchemaError("$.accounts[2]", "Object missing required field `post_count`") in errors


def test_unknown_field_is_reported() -> None:
    # ACT
    errors = validate_schema({"accounts": [account(new_field=1)]}, "fake_api.find_accounts")

    # ASSERT
    assert errors == [SchemaError("$.accounts[0].new_field", "Object contains unknown field `new_field`")]


def test_legacy_serialization_decodes_legacy_assets() -> None:
    # ARRANGE
    response = [account(balance="1.000 HIVE")]

    # ACT & ASSERT
    assert validate_schema(response, "fake_legacy_api.get_accounts") == []
    assert validate_schema(response, "fake_api.get_accounts") != []


def test_endpoint_given_as_method() -> None:
    # ARRANGE
    response = [account(balance="1.000 HIVE")]

    # ACT & ASSERT
    assert validate_schema(response, FakeLegacyApi().get_accounts) == []
    assert validate_schema(json.dumps({"accounts": [account()]}).encode(), FakeApi.find_accounts) == []


def test_public_models_are_converted_back_to_builtins() -> None:
    # ARRANGE
    response = [PublicAccount(name="Invalid!", balance=nai_hive(), post_count=1)]

    # ACT
    errors = validate_schema(response, "fake_api.get_accounts")

    # ASSERT
    assert [error.path for error in errors] == ["$[0].name"]


def test_custom_model_validates_only_its_fields() -> None:
    # ARRANGE
    class OnlyName(PreconfiguredBaseModel, forbid_unknown_fields=False):
        name: AccountName

    response = [account(post_count="not a number")]

    # ACT & ASSERT
    assert validate_schema(response, "fake_api.get_accounts", model=list[OnlyName]) == []
    assert validate_schema(response, "fake_api.get_accounts") != []


def test_unknown_endpoint_raises() -> None:
    # ACT & ASSERT
    with pytest.raises(UnknownEndpointError):
        validate_schema({}, "not_registered_api.method")
    with pytest.raises(UnknownEndpointError):
        validate_schema({}, "fake_api.not_existing_method")


def test_convert_returns_validation_model_with_hive_types() -> None:
    # ACT
    converted = convert_to_validation_schema({"accounts": [account()]}, "fake_api.find_accounts")

    # ASSERT
    assert isinstance(converted, GetAccountsResponse)
    assert isinstance(converted.accounts[0].balance, AssetHive)
    assert converted.accounts[0].balance == AssetHive(amount=1000)


def test_convert_of_legacy_response_and_endpoint_given_as_method() -> None:
    # ACT
    converted = convert_to_validation_schema([account(balance="1.000 HIVE")], FakeLegacyApi().get_accounts)

    # ASSERT
    assert converted[0].balance == AssetHive(amount=1000)


def test_convert_raises_on_invalid_response() -> None:
    # ACT & ASSERT
    with pytest.raises(ValidationError):
        convert_to_validation_schema({"accounts": [account(name="Invalid!")]}, "fake_api.find_accounts")
    with pytest.raises(UnknownEndpointError):
        convert_to_validation_schema({}, "not_registered_api.method")
