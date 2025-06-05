from __future__ import annotations

from schemas.fields.assets._base import AssetVests
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _VestingSharesSplitOperation(VirtualOperation):
    owner: AccountName
    vesting_shares_before_split: AssetVests
    vesting_shares_after_split: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "vesting_shares_split"

    @classmethod
    def vop_offset(cls) -> int:
        return 29


class VestingSharesSplitOperation(_VestingSharesSplitOperation):
    ...


class VestingSharesSplitOperationLegacy(_VestingSharesSplitOperation):
    ...
