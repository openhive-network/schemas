from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.fields.integers import Int16t
from schemas.operation import Operation

DEFAULT_WEIGHT: Final[Int16t] = Int16t(0)


class VoteOperation(Operation):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Int16t = DEFAULT_WEIGHT

    @classmethod
    def get_name(cls) -> str:
        return "vote"

    @classmethod
    def offset(cls) -> int:
        return 0
