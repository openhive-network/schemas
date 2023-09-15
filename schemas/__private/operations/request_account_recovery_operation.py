from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority
from schemas.__private.operation import Operation


class RequestAccountRecoveryOperation(Operation):
    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority
