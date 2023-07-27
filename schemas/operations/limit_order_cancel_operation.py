from __future__ import annotations

from typing import Final

from schemas.hive_fields_basic_schemas import AccountName, Uint32t
from schemas.preconfigured_base_model import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)


class LimitOrderCancelOperation(Operation):
    owner: AccountName
    order_id: Uint32t = DEFAULT_ORDER_ID
