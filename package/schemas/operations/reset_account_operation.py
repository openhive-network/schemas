from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Authority


class ResetAccountOperation(BaseModel, extra=Extra.forbid):
    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority
