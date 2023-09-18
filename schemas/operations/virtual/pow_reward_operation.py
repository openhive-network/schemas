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


class _PowRewardOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "pow_reward"

    worker: AccountName
    reward: AssetHiveT | AssetVestsT


class PowRewardOperation(_PowRewardOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class PowRewardOperationLegacy(_PowRewardOperation[AssetHiveLegacy, AssetVestsLegacy]):
    ...
