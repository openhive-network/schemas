from schemas.package.schemas.predefined import AccountName, LegacyAssetHbd, LegacyAssetHive, Uint32t
from preconfigure_base_model import PreconfiguredBaseModel


class TransferFromSavingsOperation(PreconfiguredBaseModel):
    From: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str

