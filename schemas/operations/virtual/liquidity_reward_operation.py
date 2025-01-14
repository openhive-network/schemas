from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _LiquidityRewardOperation(VirtualOperation, kw_only=True):
    owner: AccountName
    payout: AssetHive


    @classmethod
    def get_name(cls):
        return "liquidity_reward"
    
    @classmethod
    def offset(cls):
        return 4

class LiquidityRewardOperation(_LiquidityRewardOperation):
    ...


class LiquidityRewardOperationLegacy(_LiquidityRewardOperation):
    ...
