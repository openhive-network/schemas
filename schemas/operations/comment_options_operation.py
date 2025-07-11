from __future__ import annotations

from typing import Any, Final

from msgspec import field

from schemas.fields.assets._base import AssetHbd, AssetNaiAmount
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.hive_constants import HIVE_100_PERCENT
from schemas.operation import Operation

DEFAULT_ALLOW_VOTES: Final[bool] = True
DEFAULT_ALLOW_CURATION_REWARDS: Final[bool] = True
DEFAULT_MAX_ACCEPTED_PAYOUT: Final[AssetHbd] = AssetHbd(amount=AssetNaiAmount(1000000000))


class CommentOptionsOperation(Operation):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbd = field(default=DEFAULT_MAX_ACCEPTED_PAYOUT)
    percent_hbd: Uint16t = Uint16t(HIVE_100_PERCENT)
    allow_votes: bool = DEFAULT_ALLOW_VOTES
    allow_curation_rewards: bool = DEFAULT_ALLOW_CURATION_REWARDS
    extensions: list[Any] = field(default_factory=list)

    @classmethod
    def get_name(cls) -> str:
        return "comment_options"

    @classmethod
    def offset(cls) -> int:
        return 19
