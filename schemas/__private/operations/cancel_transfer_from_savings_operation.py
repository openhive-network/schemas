from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint32t
from schemas.__private.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CancelTransferFromSavingsOperation(Operation):
    from_: AccountName = Field(alias="from")
    request_id: Uint32t = DEFAULT_REQUEST_ID
