from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation


class _ProducerRewardOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "producer_reward"
    __offset__ = 14

    producer: AccountName
    vesting_shares: AssetUnion[AssetHive, AssetVest]


class ProducerRewardOperation(_ProducerRewardOperation):
    ...


class ProducerRewardOperationLegacy(_ProducerRewardOperation):
    ...
