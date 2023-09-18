from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, EmptyString
from schemas.operation import Operation


class AccountWitnessProxyOperation(Operation):
    __operation_name__ = "account_witness_proxy"

    account: AccountName
    proxy: AccountName | EmptyString
