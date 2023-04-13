from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class DeleteCommentOperation(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
