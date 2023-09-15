from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.virtual_operation import VirtualOperation


class ChangedRecoveryAccountOperation(VirtualOperation):
    account: AccountName
    old_recovery_account: AccountName
    new_recovery_account: AccountName
