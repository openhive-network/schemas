from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class CommentPayoutUpdateOperation(VirtualOperation):
    __operation_name__ = "comment_payout_update"

    author: AccountName
    permlink: str
