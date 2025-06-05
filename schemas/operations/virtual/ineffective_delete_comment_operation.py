from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class IneffectiveDeleteCommentOperation(VirtualOperation):
    author: AccountName
    permlink: str

    @classmethod
    def get_name(cls) -> str:
        return "ineffective_delete_comment"

    @classmethod
    def vop_offset(cls) -> int:
        return 23
