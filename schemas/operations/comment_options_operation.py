from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.hive_constants import HIVE_100_PERCENT
from schemas.operation import Operation

DEFAULT_ALLOW_VOTES: Final[bool] = True
DEFAULT_ALLOW_CURATION_REWARDS: Final[bool] = True
DEFAULT_MAX_ACCEPTED_PAYOUT: Final[AssetHbd] = AssetHbd(amount=1000000000)


class _CommentOptionsOperation(Operation):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbd
    percent_hbd: Uint16t = Uint16t(HIVE_100_PERCENT)
    allow_votes: bool = DEFAULT_ALLOW_VOTES
    allow_curation_rewards: bool = DEFAULT_ALLOW_CURATION_REWARDS
    extensions: list[Any] = Field(default_factory=list)


    @classmethod
    def get_name(cls):
        return "comment_options"
    
    @classmethod
    def offset(cls):
        return 19

class CommentOptionsOperation(_CommentOptionsOperation):
    max_accepted_payout: AssetHbd = Field(default_factory=DEFAULT_MAX_ACCEPTED_PAYOUT)


class CommentOptionsOperationLegacy(_CommentOptionsOperation):
    max_accepted_payout: AssetHbd = Field(default_factory=DEFAULT_MAX_ACCEPTED_PAYOUT)
