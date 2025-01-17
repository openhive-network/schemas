from __future__ import annotations



from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _TransferToVestingCompletedOperation(VirtualOperation, kw_only=True):
    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHive
    vesting_shares_received: AssetVest


    @classmethod
    def get_name(cls):
        return "transfer_to_vesting_completed"
    
    @classmethod
    def offset(cls):
        return 27

class TransferToVestingCompletedOperation(_TransferToVestingCompletedOperation):
    ...


class TransferToVestingCompletedOperationLegacy(
    _TransferToVestingCompletedOperation
):
    ...
