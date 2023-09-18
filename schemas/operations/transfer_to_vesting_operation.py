from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    EmptyString,
)
from schemas.operation import Operation


class _TransferToVestingOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "transfer_to_vesting"

    from_: AccountName = Field(alias="from")
    to: AccountName | EmptyString
    amount: AssetHiveT


class TransferToVestingOperation(_TransferToVestingOperation[AssetHiveHF26]):
    ...


class TransferToVestingOperationLegacy(_TransferToVestingOperation[AssetHiveLegacy]):
    ...
