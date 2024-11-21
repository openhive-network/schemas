from __future__ import annotations

from typing import Generic

from pydantic import BaseModel, Field

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    EmptyString,
)
from schemas.operation import Operation


class _TransferToVestingOperation(Operation, BaseModel, Generic[AssetHiveT]):
    __operation_name__ = "transfer_to_vesting"
    __offset__ = 3

    from_: AccountName = Field(alias="from")
    to: AccountName | EmptyString
    amount: AssetHiveT


class TransferToVestingOperation(_TransferToVestingOperation[AssetHiveHF26]):
    ...


class TransferToVestingOperationLegacy(_TransferToVestingOperation[AssetHiveLegacy]):
    ...
