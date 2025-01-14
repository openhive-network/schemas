from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class IneffectiveDeleteCommentOperation(VirtualOperation):
    author: AccountName
    permlink: str

    @classmethod
    def get_name(cls):
        return "ineffective_delete_comment"
    
    @classmethod
    def offset(cls):
        return 23
