from __future__ import annotations

from typing import Final

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.virtual_operation import VirtualOperation

DEFAULT_ORDERID: Final[Uint32t] = Uint32t(0)


class _LimitOrderCancelledOperation(VirtualOperation, kw_only=True):
    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetUnionAssetHiveAssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "limit_order_cancelled"

    @classmethod
    def vop_offset(cls) -> int:
        return 35


class LimitOrderCancelledOperation(_LimitOrderCancelledOperation):
    ...


class LimitOrderCancelledOperationLegacy(_LimitOrderCancelledOperation):
    ...
