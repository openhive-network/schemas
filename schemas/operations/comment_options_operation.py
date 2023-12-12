from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.hive_constants import HIVE_100_PERCENT
from schemas.operation import Operation

DEFAULT_ALLOW_VOTES: Final[bool] = True
DEFAULT_ALLOW_CURATION_REWARDS: Final[bool] = True
DEFAULT_MAX_ACCEPTED_PAYOUT: Final[AssetHbdHF26] = AssetHbdHF26(amount=1000000000)


class _CommentOptionsOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "comment_options"
    __offset__ = 19

    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbdT
    percent_hbd: Uint16t = Uint16t(HIVE_100_PERCENT)
    allow_votes: bool = DEFAULT_ALLOW_VOTES
    allow_curation_rewards: bool = DEFAULT_ALLOW_CURATION_REWARDS
    extensions: list[Any] = Field(default_factory=list)


class CommentOptionsOperation(_CommentOptionsOperation[AssetHbdHF26]):
    max_accepted_payout: AssetHbdHF26 = DEFAULT_MAX_ACCEPTED_PAYOUT


class CommentOptionsOperationLegacy(_CommentOptionsOperation[AssetHbdLegacy]):
    max_accepted_payout: AssetHbdLegacy = Field(default_factory=lambda: AssetHbdLegacy(DEFAULT_MAX_ACCEPTED_PAYOUT.as_legacy()))
