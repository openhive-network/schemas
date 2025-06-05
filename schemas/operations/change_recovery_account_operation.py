from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class ChangeRecoveryAccountOperation(Operation):
    account_to_recover: AccountName
    new_recovery_account: AccountName
    extensions: FutureExtensions = field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls) -> str:
        return "change_recovery_account"

    @classmethod
    def offset(cls) -> int:
        return 26
