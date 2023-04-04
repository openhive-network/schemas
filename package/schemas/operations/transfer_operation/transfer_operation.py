from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, PublicKey, AssetHbd, LegacyAssetHive, LegacyAssetHbd


class TransferOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHive | LegacyAssetHbd
    memo: PublicKey


