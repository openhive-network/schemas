from pydantic import Json
from typing import Optional

from schemas.__private.hive_fields_schemas import AccountName, Authority, PublicKey
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class AccountUpdateOperation(PreconfiguredBaseModel):
    account: AccountName
    owner: Optional[Authority]
    active: Optional[Authority]
    posting: Optional[Authority]
    memo_key: PublicKey
    json_metadata: Json
