from __future__ import annotations

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class LimitOrderCreateOperationStrict(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: AssetHbdLegacy | AssetHiveLegacy
    min_to_receive: AssetHbdLegacy | AssetHiveLegacy
    fill_or_kill: bool
    time_point_sec: HiveDateTime