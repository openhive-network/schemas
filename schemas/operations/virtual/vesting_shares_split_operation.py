from __future__ import annotations



from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _VestingSharesSplitOperation(VirtualOperation):
    owner: AccountName
    vesting_shares_before_split: AssetVest
    vesting_shares_after_split: AssetVest


    @classmethod
    def get_name(cls):
        return "vesting_shares_split"
    
    @classmethod
    def offset(cls):
        return 29

class VestingSharesSplitOperation(_VestingSharesSplitOperation):
    ...


class VestingSharesSplitOperationLegacy(_VestingSharesSplitOperation):
    ...
