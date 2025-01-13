from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.operation import Operation


class DeleteCommentOperation(Operation):
    author: AccountName
    permlink: str

    @classmethod
    def get_name(cls):
        return "delete_comment"
    
    @classmethod
    def offset(cls):
        return 17
