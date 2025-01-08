from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _FillVestingWithdrawOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "fill_vesting_withdraw"
    __offset__ = 6

    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVest
    deposited: AssetHive | AssetVest


class FillVestingWithdrawOperation(_FillVestingWithdrawOperation):
    ...


class FillVestingWithdrawOperationLegacy(_FillVestingWithdrawOperation):
    ...
