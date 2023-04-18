from __future__ import annotations

from typing import TYPE_CHECKING, Final

from pydantic import Field

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetHbd, LegacyAssetHive

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class TransferFromSavingsOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
