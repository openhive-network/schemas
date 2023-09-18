from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName, UShareType
from schemas.virtual_operation import VirtualOperation

DEFAULT_VOTES: Final[UShareType] = UShareType(0)


class DelayedVotingOperation(VirtualOperation):
    __operation_name__ = "delayed_voting"

    voter: AccountName
    votes: UShareType = DEFAULT_VOTES
