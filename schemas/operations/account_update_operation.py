from __future__ import annotations

from schemas.fields.basic import AccountName, PublicKey
from schemas.fields.compound import Authority
from schemas.operation import Operation


class AccountUpdateOperation(Operation):
    __operation_name__ = "account_update"

    account: AccountName
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey
    json_metadata: str
