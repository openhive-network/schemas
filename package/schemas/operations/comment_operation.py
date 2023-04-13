from __future__ import annotations

from pydantic import Json

from schemas.__private.hive_fields_schemas import AccountName, EmptyString
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

"""
If operation creates comment -> parent_author field empty string
"""


class CommentOperation(PreconfiguredBaseModel):
    parent_author: AccountName | EmptyString
    parent_permlink: str
    author: AccountName
    permlink: str
    title: str
    body: str
    json_metadata: Json
