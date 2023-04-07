from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import (AccountName, Uint32t, LegacyAssetHbd, LegacyAssetHive, HbdExchangeRate, HiveDateTime)


class LimitOrderCreate2Operation(BaseModel, extra=Extra.forbid):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: LegacyAssetHive | LegacyAssetHbd
    fill_or_kill: bool = False
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime



