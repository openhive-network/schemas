from __future__ import annotations

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation


class AccountCreateOperation(Operation):
    fee: AssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str

    @classmethod
    def get_name(cls) -> str:
        return "account_create"

    @classmethod
    def offset(cls) -> int:
        return 9
