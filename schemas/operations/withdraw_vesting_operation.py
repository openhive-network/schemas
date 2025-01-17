from __future__ import annotations



from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _WithdrawVestingOperation(Operation):
    account: AccountName
    vesting_shares: AssetVest


    @classmethod
    def get_name(cls):
        return "withdraw_vesting"
    
    @classmethod
    def offset(cls):
        return 4

class WithdrawVestingOperation(_WithdrawVestingOperation):
    ...


class WithdrawVestingOperationLegacy(_WithdrawVestingOperation):
    ...
