from __future__ import annotations

from typing import TYPE_CHECKING, Final

from pydantic import Field

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbd,
        AssetHive,
        LegacyAssetHbd,
        LegacyAssetHive,
    )

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowReleaseOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd | LegacyAssetHbd  # here add default value
    hive_amount: AssetHive | LegacyAssetHive  # here add default value
