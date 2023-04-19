from __future__ import annotations

from typing import Final

from schemas.__private.operations_strict.decline_voting_rights_operation_strict import (
    DeclineVotingRightsOperationStrict,
)

DEFAULT_DECLINE: Final[bool] = True


class DeclineVotingRightsOperation(DeclineVotingRightsOperationStrict):
    decline: bool = DEFAULT_DECLINE
