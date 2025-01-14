from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.fields.integers import UShareType
from schemas.virtual_operation import VirtualOperation

DEFAULT_VOTES: Final[UShareType] = UShareType(0)


class DelayedVotingOperation(VirtualOperation):
    voter: AccountName
    votes: UShareType = DEFAULT_VOTES

    @classmethod
    def get_name(cls):
        return "delayed_voting"
    
    @classmethod
    def offset(cls):
        return 20
