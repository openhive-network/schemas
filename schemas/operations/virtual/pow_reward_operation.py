from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation


class _PowRewardOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "pow_reward"
    __offset__ = 28

    worker: AccountName
    reward: AssetUnion[AssetHive, AssetVest]


class PowRewardOperation(_PowRewardOperation):
    ...


class PowRewardOperationLegacy(_PowRewardOperation):
    ...
