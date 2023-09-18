from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Authority,
    PublicKey,
)
from schemas.operation import Operation


class _AccountCreateOperation(Operation, GenericModel, Generic[AssetHive]):
    __operation_name__ = "account_create"

    fee: AssetHive
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
