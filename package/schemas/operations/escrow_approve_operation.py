from __future__ import annotations

from typing import TYPE_CHECKING, Final

from pydantic import Field

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)
DEFAULT_APPROVE: Final[bool] = True


class EscrowApproveOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    approve: bool = DEFAULT_APPROVE
