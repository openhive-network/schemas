from __future__ import annotations

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class LiquidityRewardOperation(VirtualOperation, kw_only=True):
    owner: AccountName
    payout: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "liquidity_reward"

    @classmethod
    def vop_offset(cls) -> int:
        return 4
