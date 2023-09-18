from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    Uint16t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class _FillRecurrentTransferOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "fill_recurrent_transfer"

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHiveT | AssetHbdT
    memo: str
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS


class FillRecurrentTransferOperation(_FillRecurrentTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillRecurrentTransferOperationLegacy(_FillRecurrentTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
