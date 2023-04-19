from __future__ import annotations

from typing import Any

from pydantic import Field, Json

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveLegacy,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EscrowTransferOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t
    hbd_amount: AssetHbd | AssetHbdLegacy
    hive_amount: AssetHive | AssetHbdLegacy
    fee: AssetHive | AssetHbd | AssetHbdLegacy | AssetHiveLegacy
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json[Any]
