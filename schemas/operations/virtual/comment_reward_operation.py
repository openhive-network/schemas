from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHbdHF26, AssetHbdLegacy, AssetHbdT, ShareType
from schemas.virtual_operation import VirtualOperation


class _CommentRewardOperation(VirtualOperation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "comment_reward"

    author: AccountName
    permlink: str
    payout: AssetHbdT
    author_rewards: ShareType
    total_payout_value: AssetHbdT
    curator_payout_value: AssetHbdT
    beneficiary_payout_value: AssetHbdT


class CommentRewardOperation(_CommentRewardOperation[AssetHbdHF26]):
    ...


class CommentRewardOperationLegacy(_CommentRewardOperation[AssetHbdLegacy]):
    ...
