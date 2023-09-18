from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _ProducerRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetVests]):
    __operation_name__ = "producer_reward"

    producer: AccountName
    vesting_shares: AssetHive | AssetVests


class ProducerRewardOperation(_ProducerRewardOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class ProducerRewardOperationLegacy(_ProducerRewardOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
