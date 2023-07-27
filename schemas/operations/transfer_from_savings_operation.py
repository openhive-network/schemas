from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.preconfigured_base_model import Operation

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class TransferFromSavingsOperation(Generic[AssetHive, AssetHbd], GenericModel, Operation):
    from_: AccountName = Field(alias="from")
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: AssetHbd | AssetHive
    memo: str
