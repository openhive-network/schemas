from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)
DEFAULT_APPROVE: Final[bool] = True


class EscrowApproveOperation(Operation):
    __operation_name__ = "escrow_approve"

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    approve: bool = DEFAULT_APPROVE
