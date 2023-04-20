from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EscrowApproveOperationStrict(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t
    approve: bool
