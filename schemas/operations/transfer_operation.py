from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion
from schemas.operation import Operation


class _TransferOperation(Operation, kw_only=True):
    __operation_name__ = "transfer"
    __offset__ = 2

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str


class TransferOperation(_TransferOperation):
    ...


class TransferOperationLegacy(_TransferOperation):
    ...
