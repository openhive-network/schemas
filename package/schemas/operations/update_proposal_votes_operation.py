from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Int64t


class UpdateProposalVotesOperation(BaseModel, extra=Extra.forbid):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool = False
    