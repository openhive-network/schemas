from __future__ import annotations

from abc import ABC
from typing import Final, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Int64t, Uint64t
from schemas.virtual_operation import VirtualOperation

DEFAULT_WEIGHT: Final[Uint64t] = Uint64t(0)
DEFAULT_RSHARES: Final[Int64t] = Int64t(0)
DEFAULT_TOTAL_VOTE_WEIGHT: Final[Uint64t] = Uint64t(0)


class Empty(BaseModel):
    pass


class _EffectiveCommentVoteOperation(VirtualOperation, GenericModel, Generic[AssetHbdT], ABC):
    __operation_name__ = "effective_comment_vote"
    __offset__ = 22

    voter: AccountName
    author: AccountName
    permlink: str
    weight: Uint64t = DEFAULT_WEIGHT
    rshares: Int64t = DEFAULT_RSHARES
    total_vote_weight: Uint64t = DEFAULT_TOTAL_VOTE_WEIGHT
    pending_payout: AssetHbdT


class EffectiveCommentVoteOperation(_EffectiveCommentVoteOperation[AssetHbdHF26]):
    ...


class EffectiveCommentVoteOperationLegacy(_EffectiveCommentVoteOperation[AssetHbdLegacy]):
    ...
