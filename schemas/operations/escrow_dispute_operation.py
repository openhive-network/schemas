from __future__ import annotations

from typing import Final


from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)

from msgspec import field

class EscrowDisputeOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID

    @classmethod
    def get_name(cls):
        return "escrow_dispute"
    
    @classmethod
    def offset(cls):
        return 28
