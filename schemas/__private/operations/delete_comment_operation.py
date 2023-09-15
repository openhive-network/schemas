from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.operation import Operation


class DeleteCommentOperation(Operation):
    author: AccountName
    permlink: str
