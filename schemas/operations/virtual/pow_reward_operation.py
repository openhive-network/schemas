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
    worker: AccountName
    reward: AssetUnion[AssetHive, AssetVest]


    @classmethod
    def get_name(cls):
        return "pow_reward"
    
    @classmethod
    def offset(cls):
        return 28

class PowRewardOperation(_PowRewardOperation):
    ...


class PowRewardOperationLegacy(_PowRewardOperation):
    ...
