from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbd,
        AssetHbdLegacy,
        AssetHive,
        AssetHiveLegacy,
        Uint32t,
    )


class EscrowReleaseOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t
    hbd_amount: AssetHbd | AssetHbdLegacy  # here add default value
    hive_amount: AssetHive | AssetHiveLegacy  # here add default value
