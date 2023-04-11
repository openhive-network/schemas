from schemas.package.schemas.predefined import AccountName, AssetVests, LegacyAssetVests
from preconfigure_base_model import PreconfiguredBaseModel


class DelegateVestingSharesOperation(PreconfiguredBaseModel):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests | LegacyAssetVests
