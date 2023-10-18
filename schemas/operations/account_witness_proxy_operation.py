from __future__ import annotations

from schemas.fields.basic import AccountName, EmptyString
from schemas.operation import Operation


class AccountWitnessProxyOperation(Operation):
    __operation_name__ = "account_witness_proxy"
    __offset__ = 13

    account: AccountName
    proxy: AccountName | EmptyString
