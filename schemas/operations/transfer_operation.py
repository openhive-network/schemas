from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.operation import Operation


class _TransferOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "transfer"
    __offset__ = 2

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHiveT | AssetHbdT
    memo: str


class TransferOperation(_TransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class TransferOperationLegacy(_TransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
