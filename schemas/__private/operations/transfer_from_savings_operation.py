from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas_strict import Uint32t
from schemas.__private.operations_strict.transfer_from_savings_operation_strict import (
    TransferFromSavingsOperationStrict,
)

DEFAULT_TYPE_ID: Final[Uint32t] = Uint32t(0)


class TransferFromSavingsOperation(TransferFromSavingsOperationStrict):
    request_id: Uint32t = DEFAULT_TYPE_ID
