from schemas.package.schemas.predefined import AccountName, LegacyAssetHbd, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class TransferToSavingsOperation(PreconfiguredBaseModel):
    From: AccountName
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
