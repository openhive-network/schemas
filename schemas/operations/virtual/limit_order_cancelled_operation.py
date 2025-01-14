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

DEFAULT_ORDERID: Final[Uint32t] = Uint32t(0)


class _LimitOrderCancelledOperation(VirtualOperation, kw_only=True):
    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetUnion[AssetHive, AssetHbd]


    @classmethod
    def get_name(cls):
        return "limit_order_cancelled"
    
    @classmethod
    def offset(cls):
        return 35

class LimitOrderCancelledOperation(_LimitOrderCancelledOperation):
    ...


class LimitOrderCancelledOperationLegacy(_LimitOrderCancelledOperation):
    ...
