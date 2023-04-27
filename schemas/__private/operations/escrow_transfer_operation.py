from __future__ import annotations

from typing import Any, Final

from pydantic import Field, Json

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    AssetHive,
    EmptyString,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowTransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetHive | AssetHbd
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json[Any] | EmptyString
