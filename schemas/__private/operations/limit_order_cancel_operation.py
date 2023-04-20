from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas_strict import Uint32t
from schemas.__private.operations_strict.limit_order_create_operation_strict import LimitOrderCreateOperationStrict

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)


class LimitOrderCancelOperation(LimitOrderCreateOperationStrict):
    order_id: Uint32t = DEFAULT_ORDER_ID
