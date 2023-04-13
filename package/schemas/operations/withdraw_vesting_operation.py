from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetVests
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class WithdrawVestingOperation(PreconfiguredBaseModel):
    account: AccountName
    vesting_shares: LegacyAssetVests
