from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_basic_schemas import AccountName, UShareType
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_VOTES: Final[UShareType] = UShareType(0)


class DelayedVotingOperation(VirtualOperation):
    voter: AccountName
    votes: UShareType = DEFAULT_VOTES