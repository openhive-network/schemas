from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName
from schemas.preconfigured_base_model import Operation


class ChangeRecoveryAccountOperation(Operation):
    account_to_recover: AccountName
    new_recovery_account: AccountName
