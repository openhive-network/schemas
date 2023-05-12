from __future__ import annotations

from typing import Any

from pydantic import Json

from schemas.__private.hive_fields_schemas import AccountName, EmptyString
from schemas.__private.preconfigured_base_model import Operation

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
    json_metadata: Json[Any] | EmptyString
