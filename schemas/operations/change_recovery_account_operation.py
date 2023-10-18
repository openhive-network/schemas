from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class ChangeRecoveryAccountOperation(Operation):
    __operation_name__ = "change_recovery_account"
    __offset__ = 26

    account_to_recover: AccountName
    new_recovery_account: AccountName
    extensions: FutureExtensions
