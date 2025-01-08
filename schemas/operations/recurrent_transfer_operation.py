from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint16t
from schemas.operation import Operation

DEFAULT_RECURRENCE: Final[Uint16t] = Uint16t(0)
DEFAULT_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class _RecurrentTransferOperation(Operation, kw_only=True):
    __operation_name__ = "recurrent_transfer"
    __offset__ = 49

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str
    recurrence: Uint16t = DEFAULT_RECURRENCE
    executions: Uint16t = DEFAULT_EXECUTIONS
    extensions: list[Any] = Field(default_factory=list)


class RecurrentTransferOperation(_RecurrentTransferOperation):
    ...


class RecurrentTransferOperationLegacy(_RecurrentTransferOperation):
    ...
