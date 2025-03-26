from __future__ import annotations

from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation


class UpdateProposalEndDate(Operation):
    @classmethod
    def get_name(cls) -> str:
        return "update_proposal_end_date"

    @classmethod
    def offset(cls) -> int:
        return -1

    end_date: HiveDateTime
