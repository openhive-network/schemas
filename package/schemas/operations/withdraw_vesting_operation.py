from schemas.package.schemas.predefined import AccountName, LegacyAssetVests
from preconfigure_base_model import PreconfiguredBaseModel


class WithdrawVestingOperation(PreconfiguredBaseModel):
    account: AccountName
    vesting_shares: LegacyAssetVests
