from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName
from schemas.preconfigured_base_model import VirtualOperation


class ChangedRecoveryAccountOperation(VirtualOperation):
    account: AccountName
    old_recovery_account: AccountName
    new_recovery_account: AccountName
