from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHbd,
        AssetHive,
        AssetVests,
        LegacyAssetHbd,
        LegacyAssetHive,
        LegacyAssetVests,
    )


class ClaimRewardBalanceOperation(PreconfiguredBaseModel):
    account: AccountName
    reward_hive: AssetHive | LegacyAssetHive
    reward_hbd: AssetHbd | LegacyAssetHbd
    reward_vests: AssetVests | LegacyAssetVests
