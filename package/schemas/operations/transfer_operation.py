from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, PublicKey, LegacyAssetHive, LegacyAssetHbd


class TransferOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHive | LegacyAssetHbd
    memo: PublicKey


