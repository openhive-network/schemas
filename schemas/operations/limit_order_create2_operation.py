from __future__ import annotations

from typing import Final

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.compound import HbdExchangeRate
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class _LimitOrderCreate2Operation(Operation, kw_only=True):
    owner: AccountName
    orderid: Uint32t
    amount_to_sell: AssetUnionAssetHiveAssetHbd
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime

    @classmethod
    def get_name(cls) -> str:
        return "limit_order_create2"

    @classmethod
    def offset(cls) -> int:
        return 21


class LimitOrderCreate2Operation(_LimitOrderCreate2Operation):
    ...


class LimitOrderCreate2OperationLegacy(_LimitOrderCreate2Operation):
    ...
