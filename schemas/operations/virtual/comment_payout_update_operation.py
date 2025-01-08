from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class CommentPayoutUpdateOperation(VirtualOperation):
    author: AccountName
    permlink: str

    @classmethod
    def get_name(cls) -> str:
        return "comment_payout_update"

    @classmethod
    def offset(cls) -> int:
        return 11
