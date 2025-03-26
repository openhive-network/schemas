from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.operation import Operation

DEFAULT_DECLINE: Final[bool] = True


class DeclineVotingRightsOperation(Operation):
    account: AccountName
    decline: bool = DEFAULT_DECLINE

    @classmethod
    def get_name(cls) -> str:
        return "decline_voting_rights"

    @classmethod
    def offset(cls) -> int:
        return 36
