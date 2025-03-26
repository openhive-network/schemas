from __future__ import annotations

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnionAssetHiveAssetVests
from schemas.virtual_operation import VirtualOperation


class _PowRewardOperation(VirtualOperation, kw_only=True):
    worker: AccountName
    reward: AssetUnionAssetHiveAssetVests

    @classmethod
    def get_name(cls) -> str:
        return "pow_reward"

    @classmethod
    def vop_offset(cls) -> int:
        return 28


class PowRewardOperation(_PowRewardOperation):
    ...


class PowRewardOperationLegacy(_PowRewardOperation):
    ...
