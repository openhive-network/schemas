from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, AssetHbdLegacy, AssetHiveLegacy, Uint16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_RECURRENCE: Final[Uint16t] = Uint16t(0)
DEFAULT_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class RecurrentTransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: AssetHbdLegacy | AssetHiveLegacy
    memo: str
    recurrence: Uint16t = DEFAULT_RECURRENCE
    executions: Uint16t = DEFAULT_EXECUTIONS
