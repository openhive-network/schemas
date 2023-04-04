from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, LegacyAssetHbd, LegacyAssetHive, PublicKey, Uint32t


class TransferFromSavingsOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: PublicKey

