from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetHbd, LegacyAssetHive


class TransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: LegacyAssetHive | LegacyAssetHbd
    memo: str
