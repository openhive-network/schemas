from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Uint8t,
    Uint16t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_CONSECUTIVE_FAILURES: Final[Uint8t] = Uint8t(0)
DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)
DEFAULT_DELETED: Final[bool] = False


class _FailedRecurrentTransferOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "failed_recurrent_transfer"

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str
    consecutive_failures: Uint8t = DEFAULT_CONSECUTIVE_FAILURES
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
    deleted: bool = DEFAULT_DELETED


class FailedRecurrentTransferOperation(_FailedRecurrentTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FailedRecurrentTransferOperationLegacy(_FailedRecurrentTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...