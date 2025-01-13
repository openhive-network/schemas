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
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str


    @classmethod
    def get_name(cls):
        return "transfer"
    
    @classmethod
    def offset(cls):
        return 2

class TransferOperation(_TransferOperation):
    ...


class TransferOperationLegacy(_TransferOperation):
    ...
