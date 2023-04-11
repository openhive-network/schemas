from pydantic import Json
from typing import Optional

from schemas.package.schemas.predefined import AccountName, Authority, PublicKey
from preconfigure_base_model import PreconfiguredBaseModel


class AccountUpdateOperation(PreconfiguredBaseModel):
    account: AccountName
    owner: Optional[Authority]
    active: Optional[Authority]
    posting: Optional[Authority]
    memo_key: PublicKey
    json_metadata: Json
