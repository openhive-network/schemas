from __future__ import annotations

from schemas.fields.assets._base import AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion, AssetUnionAssetHiveAssetVests
from schemas.virtual_operation import VirtualOperation


class _ProducerRewardOperation(VirtualOperation, kw_only=True):
    producer: AccountName
    vesting_shares: AssetUnionAssetHiveAssetVests

    @classmethod
    def get_name(cls) -> str:
        return "producer_reward"

    @classmethod
    def offset(cls) -> int:
        return 14


class ProducerRewardOperation(_ProducerRewardOperation):
    ...


class ProducerRewardOperationLegacy(_ProducerRewardOperation):
    ...
