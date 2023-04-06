from pydantic import BaseModel, Extra, Json

from schemas.predefined import AccountName, Authority, PublicKey


class CreateClaimedAccountOperation(BaseModel, extra=Extra.forbid):
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json
