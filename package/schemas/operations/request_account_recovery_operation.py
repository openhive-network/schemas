from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Authority


class RequestAccountRecoveryOperation(BaseModel, extra=Extra.forbid):
    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority

