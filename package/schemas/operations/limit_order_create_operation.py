from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Uint32t, LegacyAssetHbd, LegacyAssetHive, HiveDateTime
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class LimitOrderCreateOperation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t = 0
    amount_to_sell: LegacyAssetHbd | LegacyAssetHive
    min_to_receive: LegacyAssetHbd | LegacyAssetHive
    fill_or_kill: bool = False
    time_point_sec: HiveDateTime
