from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class ConvertOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHbd
