from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.virtual_operation import VirtualOperation


class IneffectiveDeleteCommentOperation(VirtualOperation):
    __operation_name__ = "ineffective_delete_comment"

    author: AccountName
    permlink: str
