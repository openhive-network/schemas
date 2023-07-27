from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName
from schemas.preconfigured_base_model import Operation


class SetResetAccountOperation(Operation):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
