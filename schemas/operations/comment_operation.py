from __future__ import annotations

from schemas.fields.basic import AccountName, OptionallyEmptyAccountName
from schemas.operation import Operation

"""
If operation creates comment -> parent_author field empty string
"""


class CommentOperation(Operation):
    parent_author: OptionallyEmptyAccountName
    parent_permlink: str
    author: AccountName
    permlink: str
    title: str
    body: str
    json_metadata: str

    @classmethod
    def get_name(cls) -> str:
        return "comment"

    @classmethod
    def offset(cls) -> int:
        return 1
