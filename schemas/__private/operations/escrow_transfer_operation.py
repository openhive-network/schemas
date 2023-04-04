from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field, Json
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHive,
    EmptyString,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowTransferOperation(Generic[AssetHive, AssetHbd], GenericModel, Operation):
    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetHive | AssetHbd
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json[Any] | EmptyString
