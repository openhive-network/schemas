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
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillTransferFromSavingsOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "fill_transfer_from_savings"
    __offset__ = 9

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    request_id: Uint32t = DEFAULT_REQUEST_ID
    memo: str


class FillTransferFromSavingsOperation(_FillTransferFromSavingsOperation):
    ...


class FillTransferFromSavingsOperationLegacy(_FillTransferFromSavingsOperation):
    ...
