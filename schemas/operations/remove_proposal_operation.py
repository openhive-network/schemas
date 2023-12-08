from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Int64t
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RemoveProposalOperation(Operation):
    __operation_name__ = "remove_proposal"
    __offset__ = 46

    proposal_owner: AccountName
    proposal_ids: list[Int64t]
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)
