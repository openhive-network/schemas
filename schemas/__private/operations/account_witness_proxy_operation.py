from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AccountWitnessProxyOperation(PreconfiguredBaseModel):
    account: AccountName
    proxy: AccountName