from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_basic_schemas import AccountName, Int64t
from schemas.operation import Operation

DEFAULT_APPROVE: Final[bool] = False


class UpdateProposalVotesOperation(Operation):
    __operation_name__ = "update_proposal_votes"

    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool = DEFAULT_APPROVE
