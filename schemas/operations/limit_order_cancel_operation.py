from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)


class LimitOrderCancelOperation(Operation):
    owner: AccountName
    orderid: Uint32t = DEFAULT_ORDER_ID

    @classmethod
    def get_name(cls) -> str:
        return "limit_order_cancel"

    @classmethod
    def offset(cls) -> int:
        return 6
