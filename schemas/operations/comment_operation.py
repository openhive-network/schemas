from __future__ import annotations

from schemas.fields.basic import AccountName, EmptyString
from schemas.operation import Operation

"""
If operation creates comment -> parent_author field empty string
"""


class CommentOperation(Operation):
    parent_author: AccountName | EmptyString
    parent_permlink: str
    author: AccountName
    permlink: str
    title: str
    body: str
    json_metadata: str

    @classmethod
    def get_name(cls):
        return "comment"
    
    @classmethod
    def offset(cls):
        return 1
