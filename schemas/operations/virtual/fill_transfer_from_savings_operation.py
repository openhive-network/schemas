from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.preconfigured_base_model import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class FillTransferFromSavingsOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    request_id: Uint32t = DEFAULT_REQUEST_ID
    memo: str
