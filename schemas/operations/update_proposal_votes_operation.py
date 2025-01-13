from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Int64t
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions

DEFAULT_APPROVE: Final[bool] = False


class UpdateProposalVotesOperation(Operation):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool = DEFAULT_APPROVE
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "update_proposal_votes"
    
    @classmethod
    def offset(cls):
        return 45
