from __future__ import annotations

from typing import Final

from schemas.__private.operations_strict.limit_order_create2_operation_strict import LimitOrderCreate2OperationStrict

DEFAULT_FILL_OR_KILL: Final[bool] = False


class LimitOrderCreate2Operation(LimitOrderCreate2OperationStrict):
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
