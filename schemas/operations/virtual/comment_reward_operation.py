from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHbd, AssetHbdHF26, AssetHbdLegacy, ShareType
from schemas.virtual_operation import VirtualOperation


class _CommentRewardOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    __operation_name__ = "comment_reward"

    author: AccountName
    permlink: str
    payout: AssetHbd
    author_rewards: ShareType
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    beneficiary_payout_value: AssetHbd


class CommentRewardOperation(_CommentRewardOperation[AssetHbdHF26]):
    ...


class CommentRewardOperationLegacy(_CommentRewardOperation[AssetHbdLegacy]):
    ...