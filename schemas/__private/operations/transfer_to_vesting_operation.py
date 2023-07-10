from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, EmptyString
from schemas.__private.preconfigured_base_model import Operation


class TransferToVestingOperation(Generic[AssetHive], GenericModel, Operation):
    from_: AccountName = Field(alias="from")
    to: AccountName | EmptyString
    amount: AssetHive
