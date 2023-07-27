from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint16t
from schemas.preconfigured_base_model import Operation

DEFAULT_RECURRENCE: Final[Uint16t] = Uint16t(0)
DEFAULT_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class RecurrentTransferOperation(Generic[AssetHive, AssetHbd], GenericModel, Operation):
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHbd | AssetHive
    memo: str
    recurrence: Uint16t = DEFAULT_RECURRENCE
    executions: Uint16t = DEFAULT_EXECUTIONS