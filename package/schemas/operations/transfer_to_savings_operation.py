from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, AssetHbdLegacy, AssetHiveLegacy


class TransferToSavingsOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: AssetHbdLegacy | AssetHiveLegacy
    memo: str
