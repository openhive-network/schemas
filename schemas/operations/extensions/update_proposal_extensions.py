from __future__ import annotations

from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import OperationExtension


class UpdateProposalEndDate(OperationExtension):
    @classmethod
    def get_name(cls) -> str:
        return "update_proposal_end_date"

    end_date: HiveDateTime
