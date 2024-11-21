from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation
from pydantic import BaseModel


class _AccountCreateOperation(Operation, BaseModel, Generic[AssetHiveT]):
    __operation_name__ = "account_create"
    __offset__ = 9

    fee: AssetHiveT
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str


class AccountCreateOperation(_AccountCreateOperation[AssetHiveHF26]):
    ...


class AccountCreateOperationLegacy(_AccountCreateOperation[AssetHiveLegacy]):
    ...
