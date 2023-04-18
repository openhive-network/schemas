from __future__ import annotations

from typing import TYPE_CHECKING, Final

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CancelTransferFromSavingsOperation(PreconfiguredBaseModel):
    From: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
