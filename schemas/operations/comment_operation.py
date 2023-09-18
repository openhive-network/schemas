from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, EmptyString
from schemas.__private.operation import Operation

"""
If operation creates comment -> parent_author field empty string
"""


class CommentOperation(Operation):
    __operation_name__ = "comment"

    parent_author: AccountName | EmptyString
    parent_permlink: str
    author: AccountName
    permlink: str
    title: str
    body: str
    json_metadata: str
