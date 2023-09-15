from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.__private.virtual_operation import VirtualOperation


class _FillVestingWithdrawOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetVests]):
    __operation_name__ = "fill_vesting_withdraw"

    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVests
    deposited: AssetHive | AssetVests


class FillVestingWithdrawOperationHF26(_FillVestingWithdrawOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class FillVestingWithdrawOperationLegacy(_FillVestingWithdrawOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
