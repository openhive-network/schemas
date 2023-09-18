from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.operation import Operation

DEFAULT_DECLINE: Final[bool] = True


class DeclineVotingRightsOperation(Operation):
    __operation_name__ = "decline_voting_rights"

    account: AccountName
    decline: bool = DEFAULT_DECLINE
