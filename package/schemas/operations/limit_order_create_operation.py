from __future__ import annotations

from typing import TYPE_CHECKING, Final

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        HiveDateTime,
        LegacyAssetHbd,
        LegacyAssetHive,
    )

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_FILL_OR_KILL: Final[bool] = False


class LimitOrderCreateOperation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t = DEFAULT_ORDER_ID
    amount_to_sell: LegacyAssetHbd | LegacyAssetHive
    min_to_receive: LegacyAssetHbd | LegacyAssetHive
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    time_point_sec: HiveDateTime
