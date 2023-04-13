from schemas.__private.hive_fields_schemas import AccountName, AssetVests, LegacyAssetVests
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class DelegateVestingSharesOperation(PreconfiguredBaseModel):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests | LegacyAssetVests
