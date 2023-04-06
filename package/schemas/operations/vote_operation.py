from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Int16t


class VoteOperation(BaseModel, extra=Extra.forbid):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Int16t = 0
