from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas_strict import (
    AccountName,
    AssetHbd,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveLegacy,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EscrowReleaseOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t
    hbd_amount: AssetHbd | AssetHbdLegacy  # here add default value
    hive_amount: AssetHive | AssetHiveLegacy  # here add default value
