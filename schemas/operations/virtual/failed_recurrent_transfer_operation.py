from __future__ import annotations

from typing import Any, Final

from msgspec import field

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint8t, Uint16t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.virtual_operation import VirtualOperation

DEFAULT_CONSECUTIVE_FAILURES: Final[Uint8t] = Uint8t(0)
DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)
DEFAULT_DELETED: Final[bool] = False


class _FailedRecurrentTransferOperation(VirtualOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnionAssetHiveAssetHbd
    memo: str
    consecutive_failures: Uint8t = DEFAULT_CONSECUTIVE_FAILURES
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
    deleted: bool = DEFAULT_DELETED
    extensions: list[Any] = field(default_factory=list)

    @classmethod
    def get_name(cls) -> str:
        return "failed_recurrent_transfer"

    @classmethod
    def vop_offset(cls) -> int:
        return 34


class FailedRecurrentTransferOperation(_FailedRecurrentTransferOperation):
    ...


class FailedRecurrentTransferOperationLegacy(_FailedRecurrentTransferOperation):
    ...
