from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.preconfigured_base_model import Operation


class AccountWitnessProxyOperation(Operation):
    account: AccountName
    proxy: AccountName
