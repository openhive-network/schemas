from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Int64t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class UpdateProposalVotesOperation(PreconfiguredBaseModel):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool = False
