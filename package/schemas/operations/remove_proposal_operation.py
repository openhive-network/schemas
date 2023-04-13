from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, Int64t


class RemoveProposalOperation(PreconfiguredBaseModel):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
