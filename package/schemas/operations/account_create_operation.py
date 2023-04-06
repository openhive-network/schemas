from pydantic import BaseModel, Extra, Json

from schemas.predefined import AccountName, AssetHive, LegacyAssetHive, Authority, PublicKey


class AccountCreateOperation(BaseModel, extra=Extra.forbid):
    fee: AssetHive | LegacyAssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json
