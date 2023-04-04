from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint32t
from schemas.__private.preconfigured_base_model import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowDisputeOperation(Operation):
    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
