from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation
from pydantic import BaseModel


class _AccountCreateWithDelegationOperation(Operation, BaseModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "account_create_with_delegation"
    __offset__ = 41

    fee: AssetHiveT
    delegation: AssetVestsT
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str


class AccountCreateWithDelegationOperation(_AccountCreateWithDelegationOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class AccountCreateWithDelegationOperationLegacy(
    _AccountCreateWithDelegationOperation[AssetHiveLegacy, AssetVestsLegacy]
):
    ...
