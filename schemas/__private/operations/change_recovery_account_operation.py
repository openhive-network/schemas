from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.operation import Operation


class ChangeRecoveryAccountOperation(Operation):
    account_to_recover: AccountName
    new_recovery_account: AccountName
