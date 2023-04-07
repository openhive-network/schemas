from pydantic import BaseModel, Extra

from schemas.predefined import AccountName


class SetResetAccountOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
    