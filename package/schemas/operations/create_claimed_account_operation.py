from pydantic import Json

from schemas.package.schemas.predefined import AccountName, Authority, PublicKey
from preconfigure_base_model import PreconfiguredBaseModel


class CreateClaimedAccountOperation(PreconfiguredBaseModel):
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json
