from __future__ import annotations

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import ShareType
from schemas.virtual_operation import VirtualOperation


class _CommentRewardOperation(VirtualOperation, kw_only=True):
    author: AccountName
    permlink: str
    payout: AssetHbd
    author_rewards: ShareType
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    beneficiary_payout_value: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "comment_reward"

    @classmethod
    def offset(cls) -> int:
        return 3


class CommentRewardOperation(_CommentRewardOperation):
    ...


class CommentRewardOperationLegacy(_CommentRewardOperation):
    ...
