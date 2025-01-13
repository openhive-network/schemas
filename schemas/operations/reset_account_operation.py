from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation


class ResetAccountOperation(Operation):
    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority

    @classmethod
    def get_name(cls):
        return "reset_account"
    
    @classmethod
    def offset(cls):
        return 37
