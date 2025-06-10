from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint16t
from schemas.operation import Operation
from schemas.operations.extensions.recurrent_transfer_extensions import RecurrentTransferPairId

DEFAULT_RECURRENCE: Final[Uint16t] = Uint16t(0)
DEFAULT_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class _RecurrentTransferOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "recurrent_transfer"
    __offset__ = 49

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHiveT | AssetHbdT
    memo: str
    recurrence: Uint16t = DEFAULT_RECURRENCE
    executions: Uint16t = DEFAULT_EXECUTIONS
    extensions: RecurrentTransferPairId


class RecurrentTransferOperation(_RecurrentTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class RecurrentTransferOperationLegacy(_RecurrentTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
