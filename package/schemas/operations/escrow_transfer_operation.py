from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from pydantic import Field, Json

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbd,
        AssetHive,
        HiveDateTime,
        LegacyAssetHbd,
        LegacyAssetHive,
    )

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowTransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd | LegacyAssetHbd
    hive_amount: AssetHive | LegacyAssetHbd
    fee: AssetHive | AssetHbd | LegacyAssetHbd | LegacyAssetHive
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json[Any]
