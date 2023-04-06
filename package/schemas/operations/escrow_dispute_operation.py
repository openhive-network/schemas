from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Uint32t


class EscrowDisputeOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = 30
    