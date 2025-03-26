from __future__ import annotations

from schemas.fields.assets._base import AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation


class _AccountCreateWithDelegationOperation(Operation):
    fee: AssetHive
    delegation: AssetVests
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str

    @classmethod
    def get_name(cls) -> str:
        return "account_create_with_delegation"

    @classmethod
    def offset(cls) -> int:
        return 41


class AccountCreateWithDelegationOperation(_AccountCreateWithDelegationOperation):
    ...


class AccountCreateWithDelegationOperationLegacy(_AccountCreateWithDelegationOperation):
    ...
