from schemas.package.schemas.predefined import AccountName, PublicKey, LegacyAssetHive, LegacyAssetHbd
from preconfigure_base_model import PreconfiguredBaseModel


class TransferOperation(PreconfiguredBaseModel):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHive | LegacyAssetHbd
    memo: PublicKey
