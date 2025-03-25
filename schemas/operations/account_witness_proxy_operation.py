from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.resolvables import OptionallyEmptyAccountName
from schemas.operation import Operation


class AccountWitnessProxyOperation(Operation):
    account: AccountName
    proxy: OptionallyEmptyAccountName

    @classmethod
    def get_name(cls) -> str:
        return "account_witness_proxy"

    @classmethod
    def offset(cls) -> int:
        return 13
