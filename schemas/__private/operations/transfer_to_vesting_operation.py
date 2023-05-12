from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import AccountName, AssetHive
from schemas.__private.preconfigured_base_model import Operation


class TransferToVestingOperation(Operation, GenericModel, Generic[AssetHive]):
    from_: AccountName = Field(..., alias="from")
    to: AccountName | None = None
    amount: AssetHive
