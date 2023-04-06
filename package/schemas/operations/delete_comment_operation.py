from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName


class DeleteCommentOperation(BaseModel, extra=Extra.forbid):
    author: AccountName
    permlink: str
