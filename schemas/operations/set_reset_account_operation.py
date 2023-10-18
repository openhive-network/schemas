from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.operation import Operation


class SetResetAccountOperation(Operation):
    __operation_name__ = "set_reset_account"
    __offset__ = 38

    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
