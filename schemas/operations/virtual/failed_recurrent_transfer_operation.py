from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint8t, Uint16t
from schemas.virtual_operation import VirtualOperation

DEFAULT_CONSECUTIVE_FAILURES: Final[Uint8t] = Uint8t(0)
DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)
DEFAULT_DELETED: Final[bool] = False


class _FailedRecurrentTransferOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "failed_recurrent_transfer"
    __offset__ = 34

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str
    consecutive_failures: Uint8t = DEFAULT_CONSECUTIVE_FAILURES
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
    deleted: bool = DEFAULT_DELETED


class FailedRecurrentTransferOperation(_FailedRecurrentTransferOperation):
    ...


class FailedRecurrentTransferOperationLegacy(_FailedRecurrentTransferOperation):
    ...
