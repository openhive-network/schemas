from __future__ import annotations



from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation


class _ProducerRewardOperation(VirtualOperation, kw_only=True):
    producer: AccountName
    vesting_shares: AssetUnion[AssetHive, AssetVest]


    @classmethod
    def get_name(cls):
        return "producer_reward"
    
    @classmethod
    def offset(cls):
        return 14

class ProducerRewardOperation(_ProducerRewardOperation):
    ...


class ProducerRewardOperationLegacy(_ProducerRewardOperation):
    ...
