from schemas.package.schemas.predefined import AccountName, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class TransferToVestingOperation(PreconfiguredBaseModel):
    From: AccountName
    to: AccountName | None
    amount: LegacyAssetHive
