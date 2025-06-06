from __future__ import annotations

from typing import Final

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.operation import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_FILL_OR_KILL: Final[bool] = False


class LimitOrderCreateOperation(Operation, kw_only=True):
    owner: AccountName
    orderid: Uint32t = DEFAULT_ORDER_ID
    amount_to_sell: AssetUnionAssetHiveAssetHbd
    min_to_receive: AssetUnionAssetHiveAssetHbd
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    expiration: HiveDateTime

    @classmethod
    def get_name(cls) -> str:
        return "limit_order_create"

    @classmethod
    def offset(cls) -> int:
        return 5
