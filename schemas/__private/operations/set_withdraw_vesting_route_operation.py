from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint16t
from schemas.__private.preconfigured_base_model import Operation

DEFAULT_PERCENT: Final[Uint16t] = Uint16t(0)
DEFAULT_AUTO_VEST: Final[bool] = False


class SetWithdrawVestingRouteOperation(Operation):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = DEFAULT_PERCENT
    auto_vest: bool = DEFAULT_AUTO_VEST
