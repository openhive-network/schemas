from __future__ import annotations

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnionAssetHiveAssetVests
from schemas.virtual_operation import VirtualOperation


class ProducerRewardOperation(VirtualOperation, kw_only=True):
    producer: AccountName
    vesting_shares: AssetUnionAssetHiveAssetVests

    @classmethod
    def get_name(cls) -> str:
        return "producer_reward"

    @classmethod
    def vop_offset(cls) -> int:
        return 14
