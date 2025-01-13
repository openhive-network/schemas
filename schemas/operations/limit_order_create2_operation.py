from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.compound import HbdExchangeRate
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnion
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class _LimitOrderCreate2Operation(Operation, kw_only=True):
    __operation_name__ = "limit_order_create2"
    __offset__ = 21

    owner: AccountName
    orderid: Uint32t
    amount_to_sell: AssetUnion[AssetHive, AssetHbd]
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime


class LimitOrderCreate2Operation(_LimitOrderCreate2Operation):
    ...


class LimitOrderCreate2OperationLegacy(_LimitOrderCreate2Operation):
    ...
