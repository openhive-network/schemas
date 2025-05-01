from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint8t, Uint16t
from schemas.virtual_operation import VirtualOperation

DEFAULT_CONSECUTIVE_FAILURES: Final[Uint8t] = Uint8t(0)
DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)
DEFAULT_DELETED: Final[bool] = False
DEFAULT_PAIR_ID: Final[Uint8t] = Uint8t(0)


class _FailedRecurrentTransferOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "failed_recurrent_transfer"
    __offset__ = 34

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHiveT | AssetHbdT
    memo: str
    consecutive_failures: Uint8t = DEFAULT_CONSECUTIVE_FAILURES
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
    deleted: bool = DEFAULT_DELETED
    pair_id: Uint8t = DEFAULT_PAIR_ID


class FailedRecurrentTransferOperation(_FailedRecurrentTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...

class FailedRecurrentTransferOperationLegacy(_FailedRecurrentTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...