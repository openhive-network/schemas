from __future__ import annotations

from typing import Final

from schemas.__private.operations_strict.update_proposal_votes_operation_strict import (
    UpdateProposalVotesOperationStrict,
)

DEFAULT_APPROVE: Final[bool] = False


class UpdateProposalVotesOperation(UpdateProposalVotesOperationStrict):
    approve: bool = DEFAULT_APPROVE
