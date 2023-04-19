from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, AssetHbdLegacy, AssetHiveLegacy
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class TransferToSavingsOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: AssetHbdLegacy | AssetHiveLegacy
    memo: str
