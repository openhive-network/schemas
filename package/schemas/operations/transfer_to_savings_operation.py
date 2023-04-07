from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, LegacyAssetHbd, LegacyAssetHive


class TransferToSavingsOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
