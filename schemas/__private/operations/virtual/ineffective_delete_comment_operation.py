from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.virtual_operation import VirtualOperation


class IneffectiveDeleteCommentOperation(VirtualOperation):
    author: AccountName
    permlink: str
