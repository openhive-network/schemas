from __future__ import annotations

from typing import Any, Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName, Uint16t
from schemas.hive_constants import HIVE_100_PERCENT
from schemas.operation import Operation

DEFAULT_ALLOW_VOTES: Final[bool] = True
DEFAULT_ALLOW_CURATION_REWARDS: Final[bool] = True


class _CommentOptionsOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "comment_options"

    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbdT
    percent_hbd: Uint16t = Uint16t(HIVE_100_PERCENT)
    allow_votes: bool = DEFAULT_ALLOW_VOTES
    allow_curation_rewards: bool = DEFAULT_ALLOW_CURATION_REWARDS
    extensions: list[Any] | None


class CommentOptionsOperation(_CommentOptionsOperation[AssetHbdHF26]):
    ...


class CommentOptionsOperationLegacy(_CommentOptionsOperation[AssetHbdLegacy]):
    ...
