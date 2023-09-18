from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHive, AssetHiveHF26, AssetHiveLegacy
from schemas.virtual_operation import VirtualOperation


class _LiquidityRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive]):
    __operation_name__ = "liquidity_reward"

    owner: AccountName
    payout: AssetHive


class LiquidityRewardOperation(_LiquidityRewardOperation[AssetHiveHF26]):
    ...


class LiquidityRewardOperationLegacy(_LiquidityRewardOperation[AssetHiveLegacy]):
    ...
