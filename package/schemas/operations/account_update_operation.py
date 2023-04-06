from pydantic import BaseModel, Extra, Json
from typing import Optional

from schemas.predefined import AccountName, Authority, PublicKey


class AccountUpdateOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    owner: Optional[Authority]
    active: Optional[Authority]
    posting: Optional[Authority]
    memo_key: PublicKey
    json_metadata: Json
