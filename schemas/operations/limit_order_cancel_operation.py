from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)


class LimitOrderCancelOperation(Operation):
    __operation_name__ = "limit_order_cancel"

    owner: AccountName
    order_id: Uint32t = DEFAULT_ORDER_ID
