from __future__ import annotations

from typing import Final

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CancelTransferFromSavingsOperation(Operation):
    from_: AccountName = field(name="from")
    request_id: Uint32t = DEFAULT_REQUEST_ID

    @classmethod
    def get_name(cls) -> str:
        return "cancel_transfer_from_savings"

    @classmethod
    def offset(cls) -> int:
        return 34
