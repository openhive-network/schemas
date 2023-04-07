from pydantic import BaseModel, Extra, Json
from typing import Optional

from schemas.__private.fields_schemas import AccountName, Authority, PublicKey


class AccountUpdate2Operation(BaseModel, extra=Extra.forbid):
    account: AccountName
    owner: Optional[Authority]
    active: Optional[Authority]
    posting: Optional[Authority]
    memo_key: Optional[PublicKey]
    json_metadata: Json
    posting_json_metadata: Json
