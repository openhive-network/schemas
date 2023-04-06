from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, Uint32t, LegacyAssetHbd, LegacyAssetHive


class LimitOrderCreateOperation(BaseModel, extra=Extra.forbid):
    owner: AccountName
    order_id: Uint32t = 0
    amount_to_sell: LegacyAssetHbd | LegacyAssetHive
    min_to_receive: LegacyAssetHbd | LegacyAssetHive
    fill_or_kill: bool = False
    time_point_sec: str  # ???
