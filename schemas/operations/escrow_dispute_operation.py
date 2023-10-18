from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowDisputeOperation(Operation):
    __operation_name__ = "escrow_dispute"
    __offset__ = 28

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
