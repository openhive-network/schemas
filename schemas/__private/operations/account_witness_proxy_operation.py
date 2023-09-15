from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, EmptyString
from schemas.__private.operation import Operation


class AccountWitnessProxyOperation(Operation):
    account: AccountName
    proxy: AccountName | EmptyString
