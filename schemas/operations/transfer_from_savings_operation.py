from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    Uint32t,
)
from schemas.operation import Operation

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class _TransferFromSavingsOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "transfer_from_savings"

    from_: AccountName = Field(alias="from")
    to: AccountName
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: AssetHiveT | AssetHbdT
    memo: str


class TransferFromSavingsOperation(_TransferFromSavingsOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class TransferFromSavingsOperationLegacy(_TransferFromSavingsOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
