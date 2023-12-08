from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RequestAccountRecoveryOperation(Operation):
    __operation_name__ = "request_account_recovery"
    __offset__ = 24

    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)
