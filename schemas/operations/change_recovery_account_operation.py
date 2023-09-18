from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.operation import Operation


class ChangeRecoveryAccountOperation(Operation):
    __operation_name__ = "change_recovery_account"

    account_to_recover: AccountName
    new_recovery_account: AccountName
