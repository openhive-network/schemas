from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import (AccountName,
                                              Uint32t,
                                              LegacyAssetHbd,
                                              LegacyAssetHive,
                                              HbdExchangeRateLegacyTrue,
                                              HbdExchangeRateLegacyFalse)


class LimitOrderCreate2Operation(BaseModel, extra=Extra.forbid):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: LegacyAssetHive | LegacyAssetHbd
    fill_or_kill: bool = False
    exchange_rate: HbdExchangeRateLegacyFalse | HbdExchangeRateLegacyTrue
    expiration: str  # ???



