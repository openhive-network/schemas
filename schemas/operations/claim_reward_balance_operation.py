from __future__ import annotations

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class ClaimRewardBalanceOperation(Operation):
    account: AccountName
    reward_hive: AssetHive
    reward_hbd: AssetHbd
    reward_vests: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "claim_reward_balance"

    @classmethod
    def offset(cls) -> int:
        return 39
