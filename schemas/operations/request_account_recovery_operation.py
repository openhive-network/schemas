from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation


class RequestAccountRecoveryOperation(Operation):
    __operation_name__ = "request_account_recovery"
    __offset__ = 24

    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority
