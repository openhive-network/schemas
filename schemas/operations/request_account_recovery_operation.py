from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RequestAccountRecoveryOperation(Operation):
    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "request_account_recovery"
    
    @classmethod
    def offset(cls):
        return 24
