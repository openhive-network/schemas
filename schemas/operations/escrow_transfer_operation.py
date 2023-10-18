from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field, Json
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    EmptyString,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class _EscrowTransferOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "escrow_transfer"
    __offset__ = 27

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbdT
    hive_amount: AssetHiveT
    fee: AssetHiveT | AssetHbdT
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json[Any] | EmptyString


class EscrowTransferOperation(_EscrowTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class EscrowTransferOperationLegacy(_EscrowTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
