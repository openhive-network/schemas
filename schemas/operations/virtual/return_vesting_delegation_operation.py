from __future__ import annotations

from schemas.fields.assets._base import AssetVests
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ReturnVestingDelegationOperation(VirtualOperation, kw_only=True):
    account: AccountName
    vesting_shares: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "return_vesting_delegation"

    @classmethod
    def vop_offset(cls) -> int:
        return 12
