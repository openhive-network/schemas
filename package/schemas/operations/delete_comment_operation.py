from __future__ import annotations

from schemas.package.schemas.predefined import AccountName
from preconfigure_base_model import PreconfiguredBaseModel


class DeleteCommentOperation(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
