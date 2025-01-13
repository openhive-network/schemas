from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RecoverAccountOperation(Operation):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "recover_account"
    
    @classmethod
    def offset(cls):
        return 25
