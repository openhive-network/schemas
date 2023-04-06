from __future__ import annotations

from pydantic import BaseModel, Extra, Json

from schemas.predefined import AccountName, EmptyString

"""
If operation creates comment -> parent_author field empty string
"""


class CommentOperation(BaseModel, extra=Extra.forbid):
    parent_author: AccountName | EmptyString
    parent_permlink: str
    author: AccountName
    permlink: str
    title: str
    body: str
    json_metadata: Json

