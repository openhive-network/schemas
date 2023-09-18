from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _ClearNullAccountBalanceOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    __operation_name__ = "clear_null_account_balance"

    total_cleared: list[AssetHive | AssetHbd | AssetVests]


class ClearNullAccountBalanceOperation(_ClearNullAccountBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class ClearNullAccountBalanceOperationLegacy(
    _ClearNullAccountBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
