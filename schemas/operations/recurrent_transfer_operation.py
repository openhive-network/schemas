from __future__ import annotations

from typing import Any, Final


from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint16t
from schemas.fields.resolvables import AssetUnion
from schemas.operation import Operation

DEFAULT_RECURRENCE: Final[Uint16t] = Uint16t(0)
DEFAULT_EXECUTIONS: Final[Uint16t] = Uint16t(0)
from msgspec import field


class _RecurrentTransferOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str
    recurrence: Uint16t = DEFAULT_RECURRENCE
    executions: Uint16t = DEFAULT_EXECUTIONS
    extensions: list[Any] = field(default_factory=list)


    @classmethod
    def get_name(cls):
        return "recurrent_transfer"
    
    @classmethod
    def offset(cls):
        return 49

class RecurrentTransferOperation(_RecurrentTransferOperation):
    ...


class RecurrentTransferOperationLegacy(_RecurrentTransferOperation):
    ...
