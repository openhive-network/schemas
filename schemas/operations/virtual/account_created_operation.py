from __future__ import annotations

from schemas.fields.assets._base import AssetVests
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class AccountCreatedOperation(VirtualOperation, kw_only=True):
    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVests
    initial_delegation: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "account_created"

    @classmethod
    def vop_offset(cls) -> int:
        return 30
