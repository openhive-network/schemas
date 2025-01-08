from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ChangedRecoveryAccountOperation(VirtualOperation):
    account: AccountName
    old_recovery_account: AccountName
    new_recovery_account: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "changed_recovery_account"

    @classmethod
    def offset(cls) -> int:
        return 26
