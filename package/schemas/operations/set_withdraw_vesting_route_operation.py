from __future__ import annotations

from typing import TYPE_CHECKING, Final

from schemas.__private.hive_fields_schemas import Uint16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName

DEFAULT_PERCENT: Final[Uint16t] = Uint16t(0)
DEFAULT_AUTO_VEST: Final[bool] = False


class SetWithdrawVestingRouteOperation(PreconfiguredBaseModel):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = DEFAULT_PERCENT
    auto_vest: bool = DEFAULT_AUTO_VEST
