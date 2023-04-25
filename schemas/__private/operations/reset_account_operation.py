from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Authority
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class ResetAccountOperation(PreconfiguredBaseModel):
    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority
