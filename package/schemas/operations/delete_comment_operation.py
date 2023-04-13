from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName


class DeleteCommentOperation(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
