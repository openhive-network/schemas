from pydantic import BaseModel, Extra

from schemas.predefined import (AccountName,
                                AssetHbd,
                                AssetHive,
                                AssetVests,
                                LegacyAssetHbd,
                                LegacyAssetHive,
                                LegacyAssetVests)


class ClaimRewardBalanceOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    reward_hive: AssetHive | LegacyAssetHive
    reward_hbd: AssetHbd | LegacyAssetHbd
    reward_vests: AssetVests | LegacyAssetVests


