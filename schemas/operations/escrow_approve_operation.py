from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)
DEFAULT_APPROVE: Final[bool] = True


class EscrowApproveOperation(Operation, kw_only=True):
    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    approve: bool = DEFAULT_APPROVE

    @classmethod
    def get_name(cls):
        return "escrow_approve"
    
    @classmethod
    def offset(cls):
        return 31
