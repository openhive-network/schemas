from __future__ import annotations

from schemas.fields.hive_datetime import HiveDateTime
from schemas.operations.extensions.extension import OperationExtension


class UpdateProposalEndDate(OperationExtension):
    __extension_name__ = "update_proposal_end_date"

    end_date: HiveDateTime
