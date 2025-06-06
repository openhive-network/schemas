from __future__ import annotations

from schemas.fields.assets._base import AssetVests
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class WithdrawVestingOperation(Operation):
    account: AccountName
    vesting_shares: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "withdraw_vesting"

    @classmethod
    def offset(cls) -> int:
        return 4
