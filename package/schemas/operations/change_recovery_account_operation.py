from pydantic import BaseModel, Extra

from schemas.predefined import AccountName


class ChangeRecoveryAccountOperation(BaseModel, extra=Extra.forbid):
    account_to_recover: AccountName
    new_recovery_account: AccountName
    