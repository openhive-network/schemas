from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        HbdExchangeRate,
        HiveDateTime,
        LegacyAssetHbd,
        LegacyAssetHive,
        Uint32t,
    )


class LimitOrderCreate2OperationStrict(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: LegacyAssetHive | LegacyAssetHbd
    fill_or_kill: bool
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime
