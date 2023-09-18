from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    Uint32t,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_FILL_OR_KILL: Final[bool] = False


class _LimitOrderCreateOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "limit_order_create"

    owner: AccountName
    orderid: Uint32t = DEFAULT_ORDER_ID
    amount_to_sell: AssetHiveT | AssetHbdT
    min_to_receive: AssetHiveT | AssetHbdT
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    expiration: HiveDateTime


class LimitOrderCreateOperation(_LimitOrderCreateOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class LimitOrderCreateOperationLegacy(_LimitOrderCreateOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
