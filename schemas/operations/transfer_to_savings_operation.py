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


class _TransferToSavingsOperation(Operation, kw_only=True):
    __operation_name__ = "transfer_to_savings"
    __offset__ = 32

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str


class TransferToSavingsOperation(_TransferToSavingsOperation):
    ...


class TransferToSavingsOperationLegacy(_TransferToSavingsOperation):
    ...
