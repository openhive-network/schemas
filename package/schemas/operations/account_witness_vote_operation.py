from pydantic import BaseModel, Extra

from schemas.predefined import AccountName


class AccountWitnessVoteOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    witness: AccountName
    approve: bool = True
