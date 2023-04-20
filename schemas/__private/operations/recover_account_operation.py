from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, Authority
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class RecoverAccountOperation(PreconfiguredBaseModel):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
