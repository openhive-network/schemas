from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.operation import Operation


class DeleteCommentOperation(Operation):
    __operation_name__ = "delete_comment"

    author: AccountName
    permlink: str
