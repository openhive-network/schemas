from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, LegacyAssetHbd, LegacyAssetHive, PublicKey


class TransferToSavingsOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: PublicKey
