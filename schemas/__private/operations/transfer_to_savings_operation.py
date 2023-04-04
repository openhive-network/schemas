from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive
from schemas.__private.preconfigured_base_model import Operation


class TransferToSavingsOperation(Generic[AssetHive, AssetHbd], GenericModel, Operation):
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHbd | AssetHive
    memo: str
