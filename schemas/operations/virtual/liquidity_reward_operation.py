from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.virtual_operation import VirtualOperation


class _LiquidityRewardOperation(VirtualOperation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "liquidity_reward"

    owner: AccountName
    payout: AssetHiveT


class LiquidityRewardOperation(_LiquidityRewardOperation[AssetHiveHF26]):
    ...


class LiquidityRewardOperationLegacy(_LiquidityRewardOperation[AssetHiveLegacy]):
    ...
