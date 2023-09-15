from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.operation import Operation

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class TransferFromSavingsOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    from_: AccountName = Field(alias="from")
    to: AccountName
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: AssetHive | AssetHbd
    memo: str
