from pydantic import Field

from schemas.package.schemas.predefined import AccountName, PublicKey, LegacyAssetHive, LegacyAssetHbd
from preconfigure_base_model import PreconfiguredBaseModel


class TransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: LegacyAssetHive | LegacyAssetHbd
    memo: PublicKey
