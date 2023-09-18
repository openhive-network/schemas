from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Uint32t,
)
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_ORDERID: Final[Uint32t] = Uint32t(0)


class _LimitOrderCancelledOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "limit_order_cancelled"

    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetHive | AssetHbd


class LimitOrderCancelledOperation(_LimitOrderCancelledOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class LimitOrderCancelledOperationLegacy(_LimitOrderCancelledOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
