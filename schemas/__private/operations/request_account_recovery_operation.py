from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority
from schemas.__private.operation import Operation


class RequestAccountRecoveryOperation(Operation):
    __operation_name__ = "request_account_recovery"

    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority
