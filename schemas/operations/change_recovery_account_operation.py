from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class ChangeRecoveryAccountOperation(Operation):
    account_to_recover: AccountName
    new_recovery_account: AccountName
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "change_recovery_account"
    
    @classmethod
    def offset(cls):
        return 26
