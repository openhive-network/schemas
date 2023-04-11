from pydantic import Field

from schemas.package.schemas.predefined import AccountName, Uint32t, AssetHbd, LegacyAssetHbd, AssetHive, \
    LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class EscrowReleaseOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias='from')
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd  # here add default value
    hive_amount: AssetHive | LegacyAssetHive  # here add default value
