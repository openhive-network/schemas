from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint8t, Uint16t
from schemas.preconfigured_base_model import VirtualOperation

DEFAULT_CONSECUTIVE_FAILURES: Final[Uint8t] = Uint8t(0)
DEFAULT_REMAINING_EXECUTIONS: Final[Uint16t] = Uint16t(0)
DEFAULT_DELETED: Final[bool] = False


class FailedRecurrentTransferOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    memo: str
    consecutive_failures: Uint8t = DEFAULT_CONSECUTIVE_FAILURES
    remaining_executions: Uint16t = DEFAULT_REMAINING_EXECUTIONS
    deleted: bool = DEFAULT_DELETED
