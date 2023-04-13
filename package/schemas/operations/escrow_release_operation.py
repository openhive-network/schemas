from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbd,
        AssetHive,
        LegacyAssetHbd,
        LegacyAssetHive,
        Uint32t,
    )


class EscrowReleaseOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd  # here add default value
    hive_amount: AssetHive | LegacyAssetHive  # here add default value
