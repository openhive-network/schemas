from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.resolvables import OptionallyEmpty
from schemas.operation import Operation


class AccountWitnessProxyOperation(Operation):
    account: AccountName
    proxy: OptionallyEmpty[AccountName]

    @classmethod
    def get_name(cls):
        return "account_witness_proxy"
    
    @classmethod
    def offset(cls):
        return 13
