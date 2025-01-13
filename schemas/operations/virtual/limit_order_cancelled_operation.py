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
    __operation_name__ = "limit_order_cancelled"
    __offset__ = 35

    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetUnion[AssetHive, AssetHbd]


class LimitOrderCancelledOperation(_LimitOrderCancelledOperation):
    ...


class LimitOrderCancelledOperationLegacy(_LimitOrderCancelledOperation):
    ...
