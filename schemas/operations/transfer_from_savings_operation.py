from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Uint32t,
)
from schemas.operation import Operation

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class _TransferFromSavingsOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "transfer_from_savings"

    from_: AccountName = Field(alias="from")
    to: AccountName
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: AssetHive | AssetHbd
    memo: str


class TransferFromSavingsOperation(_TransferFromSavingsOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class TransferFromSavingsOperationLegacy(_TransferFromSavingsOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
