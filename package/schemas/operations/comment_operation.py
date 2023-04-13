from __future__ import annotations

from typing import TYPE_CHECKING, Any

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from pydantic import Json

    from schemas.__private.hive_fields_schemas import AccountName, EmptyString

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
    json_metadata: Json[Any]
