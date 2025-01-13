from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.operation import Operation

DEFAULT_APPROVE: Final[bool] = True


class AccountWitnessVoteOperation(Operation):
    account: AccountName
    witness: AccountName
    approve: bool = DEFAULT_APPROVE

    @classmethod
    def get_name(cls):
        return "account_witness_vote"
    
    @classmethod
    def offset(cls):
        return 12
