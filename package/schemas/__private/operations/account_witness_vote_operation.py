from __future__ import annotations

from typing import Final

from schemas.__private.operations_strict.account_witness_vote_operation_strict import AccountWitnessVoteOperationStrict

DEFAULT_APPROVE: Final[bool] = True


class AccountWitnessVoteOperation(AccountWitnessVoteOperationStrict):
    approve: bool = DEFAULT_APPROVE
