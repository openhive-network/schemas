from __future__ import annotations

from pydantic import Field

from schemas.package.schemas.predefined import AccountName, Uint32t
from preconfigure_base_model import PreconfiguredBaseModel


class EscrowApproveOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = 30
    approve: bool = True
