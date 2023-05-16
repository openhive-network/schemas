from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.preconfigured_base_model import Operation


class SetResetAccountOperation(Operation):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
