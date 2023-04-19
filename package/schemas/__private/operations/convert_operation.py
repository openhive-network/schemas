from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.operations_strict.convert_operation_strict import ConvertOperationStrict

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class ConvertOperation(ConvertOperationStrict):
    request_id: Uint32t = DEFAULT_REQUEST_ID