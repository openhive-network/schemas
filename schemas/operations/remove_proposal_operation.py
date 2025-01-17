from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Int64t
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RemoveProposalOperation(Operation):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
    extensions: FutureExtensions = field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "remove_proposal"
    
    @classmethod
    def offset(cls):
        return 46
