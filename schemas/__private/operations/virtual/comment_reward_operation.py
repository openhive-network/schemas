from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, ShareType
from schemas.__private.preconfigured_base_model import VirtualOperation


class CommentRewardOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    author: AccountName
    permlink: str
    payout: AssetHbd
    author_rewards: ShareType
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    beneficiary_payout_value: AssetHbd
