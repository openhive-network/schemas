from __future__ import annotations

from abc import ABC
from typing import Final, Generic

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdLegacy,
    AssetHbdNai,
    Int64t,
    Uint64t,
)
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_WEIGHT: Final[Uint64t] = Uint64t(0)
DEFAULT_RSHARES: Final[Int64t] = Int64t(0)
DEFAULT_TOTAL_VOTE_WEIGHT: Final[Uint64t] = Uint64t(0)


class Empty(BaseModel):
    pass


class EffectiveCommentVoteOperation(VirtualOperation, GenericModel, ABC, Generic[AssetHbd]):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Uint64t = DEFAULT_WEIGHT
    rshares: Int64t = DEFAULT_RSHARES
    total_vote_weight: Uint64t = DEFAULT_TOTAL_VOTE_WEIGHT
    pending_payout: AssetHbd


class LegacyEffectiveCommentVoteOperation(EffectiveCommentVoteOperation[AssetHbdLegacy]):
    pending_payout: AssetHbdLegacy = Field(default_factory=lambda: AssetHbdLegacy("0.000 HBD"))

    @classmethod
    def get_class_name(cls) -> str:
        return EffectiveCommentVoteOperation.get_class_name()

    @classmethod
    def get_name(cls) -> str:
        return EffectiveCommentVoteOperation.get_name()


class NaiEffectiveCommentVoteOperation(EffectiveCommentVoteOperation[AssetHbdNai]):
    pending_payout: AssetHbdNai = Field(default_factory=lambda: AssetHbdNai(amount="0"))

    @classmethod
    def get_class_name(cls) -> str:
        return EffectiveCommentVoteOperation.get_class_name()

    @classmethod
    def get_name(cls) -> str:
        return EffectiveCommentVoteOperation.get_name()
