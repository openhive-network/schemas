from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, AssetHive, AssetVests
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class ClaimRewardBalanceOperation(PreconfiguredBaseModel):
    account: AccountName
    reward_hive: AssetHive
    reward_hbd: AssetHbd
    reward_vests: AssetVests
