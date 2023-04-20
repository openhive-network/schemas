from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas_strict import AccountName, AssetHbdLegacy, AssetHiveLegacy
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class TransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: AssetHiveLegacy | AssetHbdLegacy
    memo: str
