from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field, Json

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbd,
        AssetHive,
        HiveDateTime,
        LegacyAssetHbd,
        LegacyAssetHive,
        Uint32t,
    )


class EscrowTransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd  # to check
    hive_amount: AssetHive | LegacyAssetHbd  # to check
    fee: AssetHive | AssetHbd | LegacyAssetHbd | LegacyAssetHive
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json
