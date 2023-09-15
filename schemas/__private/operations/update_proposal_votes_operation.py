from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_basic_schemas import AccountName, Int64t
from schemas.__private.operation import Operation

DEFAULT_APPROVE: Final[bool] = False


class UpdateProposalVotesOperation(Operation):
    voter: AccountName
    proposal_ids: list[Int64t]
    approve: bool = DEFAULT_APPROVE
