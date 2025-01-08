from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import ShareType
from schemas.virtual_operation import VirtualOperation


class _CommentRewardOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "comment_reward"
    __offset__ = 3

    author: AccountName
    permlink: str
    payout: AssetHbd
    author_rewards: ShareType
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    beneficiary_payout_value: AssetHbd


class CommentRewardOperation(_CommentRewardOperation):
    ...


class CommentRewardOperationLegacy(_CommentRewardOperation):
    ...
