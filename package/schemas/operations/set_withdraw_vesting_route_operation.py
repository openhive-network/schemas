from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, Uint16t


class SetWithdrawVestingRouteOperation(PreconfiguredBaseModel):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = 0
    auto_vest: bool = False
