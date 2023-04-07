from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, LegacyAssetHive, LegacyAssetHbd, Uint16t


class RecurrentTransferOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
    recurrence: Uint16t = 0
    executions: Uint16t = 0


