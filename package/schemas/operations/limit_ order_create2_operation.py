from __future__ import annotations

from schemas.__private.hive_fields_schemas import (
    AccountName,
    Uint32t,
    LegacyAssetHbd,
    LegacyAssetHive,
    HbdExchangeRate,
    HiveDateTime,
)
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class LimitOrderCreate2Operation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: LegacyAssetHive | LegacyAssetHbd
    fill_or_kill: bool = False
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime
