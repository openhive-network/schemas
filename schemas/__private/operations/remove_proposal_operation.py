from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Int64t
from schemas.__private.operation import Operation


class RemoveProposalOperation(Operation):
    __operation_name__ = "remove_proposal"

    proposal_owner: AccountName
    proposal_ids: list[Int64t]
