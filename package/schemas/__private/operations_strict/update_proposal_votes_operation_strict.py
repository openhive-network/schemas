from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, Int64t


class UpdateProposalVotesOperationStrict(PreconfiguredBaseModel):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool
