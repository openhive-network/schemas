from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
)
from schemas.__private.operation import Operation


class _TransferOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "transfer"

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str


class TransferOperation(_TransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class TransferOperationLegacy(_TransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
