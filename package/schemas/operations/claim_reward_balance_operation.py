from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbdLegacy,
        AssetHiveLegacy,
        AssetVestsLegacy,
    )
    from schemas.types import AssetHbd, AssetHive, AssetVests


class ClaimRewardBalanceOperation(PreconfiguredBaseModel):
    account: AccountName
    reward_hive: AssetHive | AssetHiveLegacy
    reward_hbd: AssetHbd | AssetHbdLegacy
    reward_vests: AssetVests | AssetVestsLegacy
