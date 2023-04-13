from pydantic import Json
from typing import Optional

from schemas.__private.hive_fields_schemas import AccountName, Authority, PublicKey
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class AccountUpdate2Operation(PreconfiguredBaseModel):
    account: AccountName
    owner: Optional[Authority]
    active: Optional[Authority]
    posting: Optional[Authority]
    memo_key: Optional[PublicKey]
    json_metadata: Json
    posting_json_metadata: Json
