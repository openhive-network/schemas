from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_constants import HIVE_100_PERCENT
from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, Uint16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_ALLOW_VOTES: Final[bool] = True
DEFAULT_ALLOW_CURATION_REWARDS: Final[bool] = True


class CommentOptionsOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbd
    percent_hbd: Uint16t = Uint16t(HIVE_100_PERCENT)
    allow_votes: bool = DEFAULT_ALLOW_VOTES
    allow_curation_rewards: bool = DEFAULT_ALLOW_CURATION_REWARDS
    extensions: str
