from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    HbdExchangeRate,
    Uint32t,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class _LimitOrderCreate2Operation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "limit_order_create2"

    owner: AccountName
    order_id: Uint32t
    amount_to_sell: AssetHiveT | AssetHbdT
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    exchange_rate: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
    expiration: HiveDateTime


class LimitOrderCreate2Operation(_LimitOrderCreate2Operation[AssetHiveHF26, AssetHbdHF26]):
    ...


class LimitOrderCreate2OperationLegacy(_LimitOrderCreate2Operation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
