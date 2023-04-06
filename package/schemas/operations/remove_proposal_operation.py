from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Int64t


class RemoveProposalOperation(BaseModel, extra=Extra.forbid):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
