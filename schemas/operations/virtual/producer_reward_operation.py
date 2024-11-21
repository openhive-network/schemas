from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel


class _ProducerRewardOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "producer_reward"
    __offset__ = 14

    producer: AccountName
    vesting_shares: AssetHiveT | AssetVestsT


class ProducerRewardOperation(_ProducerRewardOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class ProducerRewardOperationLegacy(_ProducerRewardOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
