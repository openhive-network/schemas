from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class AccountWitnessProxyOperation(PreconfiguredBaseModel):
    account: AccountName
    proxy: AccountName
