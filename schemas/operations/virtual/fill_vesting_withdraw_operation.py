from __future__ import annotations

from schemas.fields.assets._base import AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion, AssetUnionAssetHiveAssetVests
from schemas.virtual_operation import VirtualOperation


class _FillVestingWithdrawOperation(VirtualOperation, kw_only=True):
    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVests
    deposited: AssetUnionAssetHiveAssetVests

    @classmethod
    def get_name(cls) -> str:
        return "fill_vesting_withdraw"

    @classmethod
    def offset(cls) -> int:
        return 6


class FillVestingWithdrawOperation(_FillVestingWithdrawOperation):
    ...


class FillVestingWithdrawOperationLegacy(_FillVestingWithdrawOperation):
    ...
