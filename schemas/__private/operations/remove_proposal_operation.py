from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, Int64t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class RemoveProposalOperation(PreconfiguredBaseModel):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
