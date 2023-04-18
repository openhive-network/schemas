from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetHive, Uint32t


class CollateralizedConvertOperation(PreconfiguredBaseModel):
    owner: AccountName
    request_id: Uint32t = 0  # type: ignore
    amount: LegacyAssetHive
