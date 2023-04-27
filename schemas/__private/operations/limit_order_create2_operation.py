from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    HbdExchangeRate,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_FILL_OR_KILL: Final[bool] = False


class LimitOrderCreate2Operation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: AssetHiveLegacy | AssetHbdLegacy
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime
