from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Int64t
from schemas.__private.preconfigured_base_model import Operation


class RemoveProposalOperation(Operation):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
