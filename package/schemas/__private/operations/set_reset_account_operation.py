from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class SetResetAccountOperation(PreconfiguredBaseModel):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
