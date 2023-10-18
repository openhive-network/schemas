from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation


class ResetAccountOperation(Operation):
    __operation_name__ = "reset_account"
    __offset__ = 37

    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority
