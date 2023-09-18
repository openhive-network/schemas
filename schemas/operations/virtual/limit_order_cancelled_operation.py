from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    Uint32t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_ORDERID: Final[Uint32t] = Uint32t(0)


class _LimitOrderCancelledOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "limit_order_cancelled"

    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetHiveT | AssetHbdT


class LimitOrderCancelledOperation(_LimitOrderCancelledOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class LimitOrderCancelledOperationLegacy(_LimitOrderCancelledOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
