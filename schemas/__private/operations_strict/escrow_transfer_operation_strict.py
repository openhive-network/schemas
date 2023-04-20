from __future__ import annotations

from typing import Any

from pydantic import Field, Json

from schemas.__private.hive_fields_schemas_strict import (
    AccountName,
    AssetHbd,
    AssetHive,
    EmptyString,
    HiveDateTimeStrict,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EscrowTransferOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetHive | AssetHbd
    ratification_deadline: HiveDateTimeStrict
    escrow_expiration: HiveDateTimeStrict
    json_meta: Json[Any] | EmptyString
