from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation


class _FillVestingWithdrawOperation(VirtualOperation, kw_only=True):
    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVest
    deposited: AssetUnion[AssetHive, AssetVest]


    @classmethod
    def get_name(cls):
        return "fill_vesting_withdraw"
    
    @classmethod
    def offset(cls):
        return 6

class FillVestingWithdrawOperation(_FillVestingWithdrawOperation):
    ...


class FillVestingWithdrawOperationLegacy(_FillVestingWithdrawOperation):
    ...
