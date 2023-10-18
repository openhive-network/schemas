from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.operation import Operation

DEFAULT_APPROVE: Final[bool] = True


class AccountWitnessVoteOperation(Operation):
    __operation_name__ = "account_witness_vote"
    __offset__ = 12

    account: AccountName
    witness: AccountName
    approve: bool = DEFAULT_APPROVE
