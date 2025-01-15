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
from msgspec import field


class _FillTransferFromSavingsOperation(VirtualOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    request_id: Uint32t = DEFAULT_REQUEST_ID
    memo: str

    @classmethod
    def get_name(cls):
        return "fill_transfer_from_savings"
    
    @classmethod
    def offset(cls):
        return 9


class FillTransferFromSavingsOperation(_FillTransferFromSavingsOperation):
    ...


class FillTransferFromSavingsOperationLegacy(_FillTransferFromSavingsOperation):
    ...
