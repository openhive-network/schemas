from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    AssetVestsHF26,
    AssetVestsLegacy,
    AssetVestsT,
)
from schemas.virtual_operation import VirtualOperation


class _ProducerRewardOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "producer_reward"

    producer: AccountName
    vesting_shares: AssetHiveT | AssetVestsT


class ProducerRewardOperation(_ProducerRewardOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class ProducerRewardOperationLegacy(_ProducerRewardOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
