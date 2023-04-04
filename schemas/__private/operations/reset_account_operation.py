from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority
from schemas.__private.preconfigured_base_model import Operation


class ResetAccountOperation(Operation):
    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority
