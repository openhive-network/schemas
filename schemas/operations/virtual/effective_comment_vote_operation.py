from __future__ import annotations

from abc import ABC
from typing import Final, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_string_int import HiveStringInt
from schemas.fields.hive_string_uint import HiveStringUint
from schemas.virtual_operation import VirtualOperation

DEFAULT_WEIGHT: Final[HiveStringUint] = HiveStringUint(0)
DEFAULT_RSHARES: Final[HiveStringInt] = HiveStringInt(0)
DEFAULT_TOTAL_VOTE_WEIGHT: Final[HiveStringUint] = HiveStringUint(0)


class Empty(BaseModel):
    pass


class _EffectiveCommentVoteOperation(VirtualOperation, GenericModel, Generic[AssetHbdT], ABC):
    __operation_name__ = "effective_comment_vote"
    __offset__ = 22

    voter: AccountName
    author: AccountName
    permlink: str
    weight: HiveStringUint = DEFAULT_WEIGHT
    rshares: HiveStringInt = DEFAULT_RSHARES
    total_vote_weight: HiveStringUint = DEFAULT_TOTAL_VOTE_WEIGHT
    pending_payout: AssetHbdT


class EffectiveCommentVoteOperation(_EffectiveCommentVoteOperation[AssetHbdHF26]):
    ...


class EffectiveCommentVoteOperationLegacy(_EffectiveCommentVoteOperation[AssetHbdLegacy]):
    ...
