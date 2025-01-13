from __future__ import annotations

from schemas.fields.basic import AccountName, PublicKey
from schemas.fields.compound import Authority
from schemas.operation import Operation


class AccountUpdateOperation(Operation):
    account: AccountName
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey | None = None
    json_metadata: str | None = None

    @classmethod
    def get_name(cls):
        return "account_update"
    
    @classmethod
    def offset(cls):
        return 10
