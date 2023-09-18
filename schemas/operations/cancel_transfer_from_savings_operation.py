from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.fields.basic import AccountName, Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CancelTransferFromSavingsOperation(Operation):
    __operation_name__ = "cancel_transfer_from_savings"

    from_: AccountName = Field(alias="from")
    request_id: Uint32t = DEFAULT_REQUEST_ID
