from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.operation import Operation


class DeleteCommentOperation(Operation):
    __operation_name__ = "delete_comment"
    __offset__ = 17

    author: AccountName
    permlink: str
