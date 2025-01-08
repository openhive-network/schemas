from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class _EscrowTransferOperation(Operation, kw_only=True):
    __operation_name__ = "escrow_transfer"
    __offset__ = 27

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetHive | AssetHbd
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: str


class EscrowTransferOperation(_EscrowTransferOperation):
    ...


class EscrowTransferOperationLegacy(_EscrowTransferOperation):
    ...
