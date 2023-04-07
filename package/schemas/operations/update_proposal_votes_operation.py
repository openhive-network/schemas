from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, Uint32t


class UpdateProposalVotesOperation(BaseModel, extra=Extra.forbid):
    voter: AccountName
    proposal_ids: Uint32t
    approve: bool = False
    