from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _FillVestingWithdrawOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "fill_vesting_withdraw"
    __offset__ = 6

    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVestsT
    deposited: AssetHiveT | AssetVestsT


class FillVestingWithdrawOperation(_FillVestingWithdrawOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class FillVestingWithdrawOperationLegacy(_FillVestingWithdrawOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
