from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.operation import Operation


class SetResetAccountOperation(Operation):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "set_reset_account"

    @classmethod
    def offset(cls) -> int:
        return 38
