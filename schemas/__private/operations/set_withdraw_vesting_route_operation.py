from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import Uint16t
from schemas.__private.operations_strict.set_withdraw_vesting_route_operation_strict import (
    SetWithdrawVestingRouteOperationStrict,
)

DEFAULT_PERCENT: Final[Uint16t] = Uint16t(0)
DEFAULT_AUTO_VEST: Final[bool] = False


class SetWithdrawVestingRouteOperation(SetWithdrawVestingRouteOperationStrict):
    percent: Uint16t = DEFAULT_PERCENT
    auto_vest: bool = DEFAULT_AUTO_VEST
