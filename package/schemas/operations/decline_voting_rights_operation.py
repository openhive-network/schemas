from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName


class DeclineVotingRightsOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    decline: bool = True
