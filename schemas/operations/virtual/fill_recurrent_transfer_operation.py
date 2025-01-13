from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint16t
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation

DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class _FillRecurrentTransferOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "fill_recurrent_transfer"
    __offset__ = 33

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS


class FillRecurrentTransferOperation(_FillRecurrentTransferOperation):
    ...


class FillRecurrentTransferOperationLegacy(_FillRecurrentTransferOperation):
    ...
