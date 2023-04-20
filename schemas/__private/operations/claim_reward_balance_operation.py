from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import (
    AccountName,
    AssetHbd,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsLegacy,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class ClaimRewardBalanceOperation(PreconfiguredBaseModel):
    account: AccountName
    reward_hive: AssetHive | AssetHiveLegacy
    reward_hbd: AssetHbd | AssetHbdLegacy
    reward_vests: AssetVests | AssetVestsLegacy
