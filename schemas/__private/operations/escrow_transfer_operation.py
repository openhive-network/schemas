from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field, Json
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    EmptyString,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class _EscrowTransferOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "escrow_transfer"

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


class EscrowTransferOperation(_EscrowTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class EscrowTransferOperationLegacy(_EscrowTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
