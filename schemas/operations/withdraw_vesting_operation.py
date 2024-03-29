from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _WithdrawVestingOperation(Operation, GenericModel, Generic[AssetVestsT]):
    __operation_name__ = "withdraw_vesting"
    __offset__ = 4

    account: AccountName
    vesting_shares: AssetVestsT


class WithdrawVestingOperation(_WithdrawVestingOperation[AssetVestsHF26]):
    ...


class WithdrawVestingOperationLegacy(_WithdrawVestingOperation[AssetVestsLegacy]):
    ...
