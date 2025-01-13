from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnion
from schemas.operation import Operation

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class _TransferFromSavingsOperation(Operation, kw_only=True):
    __operation_name__ = "transfer_from_savings"
    __offset__ = 33

    from_: AccountName = Field(alias="from")
    to: AccountName
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str


class TransferFromSavingsOperation(_TransferFromSavingsOperation):
    ...


class TransferFromSavingsOperationLegacy(_TransferFromSavingsOperation):
    ...
