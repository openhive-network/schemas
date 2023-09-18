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
    HiveDateTime,
    Uint32t,
)
from schemas.__private.operation import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_FILL_OR_KILL: Final[bool] = False


class _LimitOrderCreateOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "limit_order_create"

    owner: AccountName
    orderid: Uint32t = DEFAULT_ORDER_ID
    amount_to_sell: AssetHive | AssetHbd
    min_to_receive: AssetHive | AssetHbd
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    expiration: HiveDateTime


class LimitOrderCreateOperation(_LimitOrderCreateOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class LimitOrderCreateOperationLegacy(_LimitOrderCreateOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
