from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdNai,
    Int64t,
    Uint64t,
)
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_WEIGHT: Final[Uint64t] = Uint64t(0)
DEFAULT_RSHARES: Final[Int64t] = Int64t(0)
DEFAULT_TOTAL_VOTE_WEIGHT: Final[Uint64t] = Uint64t(0)


class EffectiveCommentVoteOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Uint64t = DEFAULT_WEIGHT
    rshares: Int64t = DEFAULT_RSHARES
    total_vote_weight: Uint64t = DEFAULT_TOTAL_VOTE_WEIGHT
    pending_payout: AssetHbd = Field(default_factory=lambda: AssetHbdNai(amount=0))  # type: ignore
