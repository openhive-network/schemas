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


class _PowRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetVests]):
    __operation_name__ = "pow_reward"

    worker: AccountName
    reward: AssetHive | AssetVests


class PowRewardOperation(_PowRewardOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class PowRewardOperationLegacy(_PowRewardOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
