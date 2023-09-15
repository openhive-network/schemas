from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, AssetHiveHF26, AssetHiveLegacy
from schemas.__private.virtual_operation import VirtualOperation


class _LiquidityRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive]):
    __operation_name__ = "liquidity_reward"

    owner: AccountName
    payout: AssetHive


class LiquidityRewardOperationHF26(_LiquidityRewardOperation[AssetHiveHF26]):
    ...


class LiquidityRewardOperationLegacy(_LiquidityRewardOperation[AssetHiveLegacy]):
    ...
