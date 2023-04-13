from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetHbd, Uint32t


class ConvertOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t = 0
    amount: LegacyAssetHbd
