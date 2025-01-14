from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation

DEFAULT_CURRENT_ORDERID: Final[Uint32t] = Uint32t(0)
DEFAULT_OPEN_ORDERID: Final[Uint32t] = Uint32t(0)


class _FillOrderOperation(VirtualOperation, kw_only=True):
    current_owner: AccountName
    current_orderid: Uint32t = DEFAULT_CURRENT_ORDERID
    current_pays: AssetUnion[AssetHive, AssetHbd]
    open_owner: AccountName
    open_orderid: Uint32t = DEFAULT_OPEN_ORDERID
    open_pays: AssetUnion[AssetHive, AssetHbd]


    @classmethod
    def get_name(cls):
        return "fill_order"
    
    @classmethod
    def offset(cls):
        return 7

class FillOrderOperation(_FillOrderOperation):
    ...


class FillOrderOperationLegacy(_FillOrderOperation):
    ...
