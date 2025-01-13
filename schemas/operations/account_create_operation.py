from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
# from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation


class _AccountCreateOperation(Operation):
    fee: AssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str

    @classmethod
    def get_name(cls):
        return "account_create"
    
    @classmethod
    def offset(cls):
        return 9


class AccountCreateOperation(_AccountCreateOperation):
    ...


class AccountCreateOperationLegacy(_AccountCreateOperation):
    ...
