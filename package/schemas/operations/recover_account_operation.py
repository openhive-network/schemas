from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Authority


class RecoverAccountOperation(BaseModel, extra=Extra.forbid):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
    