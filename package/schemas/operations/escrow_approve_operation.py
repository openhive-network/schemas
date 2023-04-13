from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, Uint32t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class EscrowApproveOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = 30
    approve: bool = True
