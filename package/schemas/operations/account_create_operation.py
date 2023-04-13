from pydantic import Json

from schemas.__private.hive_fields_schemas import AccountName, AssetHive, LegacyAssetHive, Authority, PublicKey
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class AccountCreateOperation(PreconfiguredBaseModel):
    fee: AssetHive | LegacyAssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json
