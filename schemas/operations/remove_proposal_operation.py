from __future__ import annotations

from schemas.fields.basic import AccountName, Int64t
from schemas.operation import Operation


class RemoveProposalOperation(Operation):
    __operation_name__ = "remove_proposal"

    proposal_owner: AccountName
    proposal_ids: list[Int64t]