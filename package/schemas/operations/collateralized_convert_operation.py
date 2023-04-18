from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.operations_strict.collateralized_convert_operation_strict import (
    CollateralizedConvertOperationStrict,
)

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CollateralizedConvertOperation(CollateralizedConvertOperationStrict):
    request_id: Uint32t = DEFAULT_REQUEST_ID
