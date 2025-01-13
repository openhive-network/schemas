from __future__ import annotations

from schemas.fields.basic import AccountName, EmptyString
from schemas.operation import Operation


class AccountWitnessProxyOperation(Operation):
    account: AccountName
    proxy: AccountName | EmptyString

    @classmethod
    def get_name(cls):
        return "account_witness_proxy"
    
    @classmethod
    def offset(cls):
        return 13
