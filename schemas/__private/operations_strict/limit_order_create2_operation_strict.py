from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    HbdExchangeRate,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class LimitOrderCreate2OperationStrict(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: AssetHiveLegacy | AssetHbdLegacy
    fill_or_kill: bool
    exchange_rate: HbdExchangeRate
    expiration: HiveDateTime
