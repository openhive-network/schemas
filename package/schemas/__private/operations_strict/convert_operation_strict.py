from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, AssetHbdLegacy, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class ConvertOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t
    amount: AssetHbdLegacy
