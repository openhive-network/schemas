from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _LiquidityRewardOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "liquidity_reward"
    __offset__ = 4

    owner: AccountName
    payout: AssetHive


class LiquidityRewardOperation(_LiquidityRewardOperation):
    ...


class LiquidityRewardOperationLegacy(_LiquidityRewardOperation):
    ...
