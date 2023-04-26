from __future__ import annotations

from typing import Any

import pytest
from pydantic import BaseModel

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    AssetHive,
    AssetVests,
    Authority,
    HbdExchangeRate,
    HiveInt,
)


class HiveIntModel(BaseModel):
    field: HiveInt


@pytest.mark.parametrize(
    "model, value",
    [
        # AccountName
        (AccountName, "account-name"),
        (AccountName, "account---name"),
        (AccountName, "account.name"),
        # AssetHbd
        (AssetHbd, {"amount": "100", "precision": 3, "nai": "@@000000013"}),
        # AssetHive
        (AssetHive, {"amount": "100", "precision": 3, "nai": "@@000000021"}),
        # AssetVests
        (AssetVests, {"amount": "100", "precision": 6, "nai": "@@000000037"}),
        # Authority
        (
            Authority,
            {
                "weight_threshold": 1,
                "account_auths": [["alice", 1]],
                "key_auths": [["STM7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZVK9wd53t2qXCvxmB", 1]],
            },
        ),
        #  HbdExchangeRate
        (
            HbdExchangeRate,
            {
                "base": {"amount": "100", "precision": 3, "nai": "@@000000013"},
                "quote": {"amount": "100", "precision": 3, "nai": "@@000000021"},
            },
        ),
        (
            HbdExchangeRate,
            {
                "base": {"amount": "100", "precision": 3, "nai": "@@000000021"},
                "quote": {"amount": "100", "precision": 3, "nai": "@@000000021"},
            },
        ),
        (HbdExchangeRate, {"base": "0.667 HBD", "quote": "1.000 HIVE"}),
        (
            HbdExchangeRate,
            {
                "base": "0.667 HIVE",
                "quote": "1.000 HIVE",
            },
        ),
    ],
)
def test_validation_of_correct_type(model: type, value: Any) -> None:
    # ARRANGE
    class MockModel(BaseModel):
        field: model  # type: ignore

    # ACT & ASSERT
    MockModel(field=value)
