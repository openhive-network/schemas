from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation


class _AccountCreateWithDelegationOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "account_create_with_delegation"
    __offset__ = 41

    fee: AssetHiveT
    delegation: AssetHiveT
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
    extensions: Any


class AccountCreateWithDelegationOperation(_AccountCreateWithDelegationOperation[AssetHiveHF26]):
    ...


class AccountCreateWithDelegationOperationLegacy(_AccountCreateWithDelegationOperation[AssetHiveLegacy]):
    ...
