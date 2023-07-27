from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, Authority
from schemas.preconfigured_base_model import Operation


class RecoverAccountOperation(Operation):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
