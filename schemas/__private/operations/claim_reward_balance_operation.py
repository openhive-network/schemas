from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.hive_fields_schemas_strict import AssetHbdStrict, AssetHiveStrict, AssetVestsStrict
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class ClaimRewardBalanceOperation(PreconfiguredBaseModel):
    account: AccountName
    reward_hive: AssetHiveStrict
    reward_hbd: AssetHbdStrict
    reward_vests: AssetVestsStrict
