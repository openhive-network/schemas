from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetHbd, LegacyAssetHive, Uint32t


class TransferFromSavingsOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t = 0  # type: ignore
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
