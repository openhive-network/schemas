from __future__ import annotations

from typing import Final

from msgspec import field

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint16t
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation

DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class _FillRecurrentTransferOperation(VirtualOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS

    @classmethod
    def get_name(cls) -> str:
        return "fill_recurrent_transfer"

    @classmethod
    def offset(cls) -> int:
        return 33


class FillRecurrentTransferOperation(_FillRecurrentTransferOperation):
    ...


class FillRecurrentTransferOperationLegacy(_FillRecurrentTransferOperation):
    ...
