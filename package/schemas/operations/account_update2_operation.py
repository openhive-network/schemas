from pydantic import BaseModel, Extra, Json
from typing import Optional

from schemas.predefined import AccountName, Authority, PublicKey


class AccountUpdate2Operation(BaseModel, extra=Extra.forbid):
    account: AccountName
    owner: Optional[Authority]
    active: Optional[Authority]
    posting: Optional[Authority]
    memo_key: Optional[PublicKey]
    json_metadata: Json
    posting_json_metadata: Json
