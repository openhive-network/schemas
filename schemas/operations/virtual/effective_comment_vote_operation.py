from __future__ import annotations

from abc import ABC
from typing import Final, Generic

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    Int64t,
    Uint64t,
)
from schemas.preconfigured_base_model import VirtualOperation

DEFAULT_WEIGHT: Final[Uint64t] = Uint64t(0)
DEFAULT_RSHARES: Final[Int64t] = Int64t(0)
DEFAULT_TOTAL_VOTE_WEIGHT: Final[Uint64t] = Uint64t(0)


class Empty(BaseModel):
    pass


class EffectiveCommentVoteOperation(Generic[AssetHbd], GenericModel, VirtualOperation, ABC):
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


class NaiEffectiveCommentVoteOperation(EffectiveCommentVoteOperation[AssetHbdHF26]):
    pending_payout: AssetHbdHF26 = Field(default_factory=lambda: AssetHbdHF26(amount="0"))

    @classmethod
    def get_class_name(cls) -> str:
        return EffectiveCommentVoteOperation.get_class_name()

    @classmethod
    def get_name(cls) -> str:
        return EffectiveCommentVoteOperation.get_name()
