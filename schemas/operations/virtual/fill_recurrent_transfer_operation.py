from __future__ import annotations

from typing import Any, Final

from msgspec import field

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint16t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.virtual_operation import VirtualOperation

DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class FillRecurrentTransferOperation(VirtualOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnionAssetHiveAssetHbd
    memo: str
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
    extensions: list[Any] = field(default_factory=list)

    @classmethod
    def get_name(cls) -> str:
        return "fill_recurrent_transfer"

    @classmethod
    def vop_offset(cls) -> int:
        return 33
