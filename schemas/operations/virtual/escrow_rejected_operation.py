from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _EscrowRejectedOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "escrow_rejected"
    __offset__ = 40

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_REQUEST_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetHive | AssetHbd


class EscrowRejectedOperation(_EscrowRejectedOperation):
    ...


class EscrowRejectedOperationLegacy(_EscrowRejectedOperation):
    ...
