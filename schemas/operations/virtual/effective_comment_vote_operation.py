from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Int64t, Uint64t
from schemas.virtual_operation import VirtualOperation

DEFAULT_WEIGHT: Final[Uint64t] = Uint64t(0)
DEFAULT_RSHARES: Final[Int64t] = Int64t(0)
DEFAULT_TOTAL_VOTE_WEIGHT: Final[Uint64t] = Uint64t(0)


class _EffectiveCommentVoteOperation(VirtualOperation, kw_only=True):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Uint64t = DEFAULT_WEIGHT
    rshares: Int64t = DEFAULT_RSHARES
    total_vote_weight: Uint64t = DEFAULT_TOTAL_VOTE_WEIGHT
    pending_payout: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "effective_comment_vote"

    @classmethod
    def offset(cls) -> int:
        return 22


class EffectiveCommentVoteOperation(_EffectiveCommentVoteOperation):
    ...


class EffectiveCommentVoteOperationLegacy(_EffectiveCommentVoteOperation):
    ...
