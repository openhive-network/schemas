from pydantic import BaseModel, Extra, Json

from schemas.__private.fields_schemas import AccountName, Authority, PublicKey


class AccountUpdate2Operation(BaseModel, extra=Extra.forbid):
    account: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json
    posting_json_metadata: Json
