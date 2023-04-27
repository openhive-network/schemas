from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import AccountName, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)


class LimitOrderCancelOperation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t = DEFAULT_ORDER_ID
