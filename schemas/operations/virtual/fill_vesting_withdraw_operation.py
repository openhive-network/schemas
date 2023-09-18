from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    AssetVestsHF26,
    AssetVestsLegacy,
    AssetVestsT,
)
from schemas.virtual_operation import VirtualOperation


class _FillVestingWithdrawOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "fill_vesting_withdraw"

    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVestsT
    deposited: AssetHiveT | AssetVestsT


class FillVestingWithdrawOperation(_FillVestingWithdrawOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class FillVestingWithdrawOperationLegacy(_FillVestingWithdrawOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
