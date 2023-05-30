from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint16t
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class FillRecurrentTransferOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
