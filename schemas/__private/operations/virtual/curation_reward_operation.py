from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class CurationRewardOperation(Generic[AssetVests], GenericModel, VirtualOperation):
    curator: AccountName
    reward: AssetVests
    comment_author: AccountName
    comment_permlink: str
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED
