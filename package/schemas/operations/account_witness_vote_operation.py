from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName


class AccountWitnessVoteOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    witness: AccountName
    approve: bool = True
