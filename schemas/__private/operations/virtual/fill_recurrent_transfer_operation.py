from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Uint16t,
)
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class _FillRecurrentTransferOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "fill_recurrent_transfer"

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS


class FillRecurrentTransferOperationHF26(_FillRecurrentTransferOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillRecurrentTransferOperationLegacy(_FillRecurrentTransferOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
