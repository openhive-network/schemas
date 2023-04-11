from __future__ import annotations

from schemas.package.schemas.predefined import AccountName, Int64t
from preconfigure_base_model import PreconfiguredBaseModel


class UpdateProposalVotesOperation(PreconfiguredBaseModel):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool = False
    