from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        HiveDateTime,
        LegacyAssetHbd,
        LegacyAssetHive,
        Uint32t,
    )


class LimitOrderCreateOperationStrict(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: LegacyAssetHbd | LegacyAssetHive
    min_to_receive: LegacyAssetHbd | LegacyAssetHive
    fill_or_kill: bool
    time_point_sec: HiveDateTime
