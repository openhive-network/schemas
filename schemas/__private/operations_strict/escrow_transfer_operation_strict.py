from __future__ import annotations

from typing import Any

from pydantic import Field, Json

from schemas.__private.hive_fields_schemas import (
    AccountName,
    EmptyString,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.hive_fields_schemas_strict import AssetHbdStrict, AssetHiveStrict
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EscrowTransferOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t
    hbd_amount: AssetHbdStrict
    hive_amount: AssetHiveStrict
    fee: AssetHiveStrict | AssetHbdStrict
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json[Any] | EmptyString
