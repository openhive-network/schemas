from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, LegacyAssetHbd, LegacyAssetHive, Uint32t


class TransferFromSavingsOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str

