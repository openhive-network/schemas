from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_ORDERID: Final[Uint32t] = Uint32t(0)


class _LimitOrderCancelledOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "limit_order_cancelled"
    __offset__ = 35

    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetHiveT | AssetHbdT


class LimitOrderCancelledOperation(_LimitOrderCancelledOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class LimitOrderCancelledOperationLegacy(_LimitOrderCancelledOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
