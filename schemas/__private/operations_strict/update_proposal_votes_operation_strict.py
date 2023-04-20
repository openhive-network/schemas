from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Int64t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class UpdateProposalVotesOperationStrict(PreconfiguredBaseModel):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool