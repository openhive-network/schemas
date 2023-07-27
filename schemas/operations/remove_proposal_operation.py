from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, Int64t
from schemas.preconfigured_base_model import Operation


class RemoveProposalOperation(Operation):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
