from __future__ import annotations

from schemas.fields.assets._base import AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class TransferToVestingCompletedOperation(VirtualOperation, kw_only=True):
    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHive
    vesting_shares_received: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "transfer_to_vesting_completed"

    @classmethod
    def vop_offset(cls) -> int:
        return 27
