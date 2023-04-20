from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas_strict import Uint16t
from schemas.__private.operations_strict.recurrent_transfer_operation_strict import RecurrentTransferOperationStrict

DEFAULT_RECURRENCE: Final[Uint16t] = Uint16t(0)
DEFAULT_EXECUTIONS: Final[Uint16t] = Uint16t(0)


class RecurrentTransferOperation(RecurrentTransferOperationStrict):
    recurrence: Uint16t = DEFAULT_RECURRENCE
    executions: Uint16t = DEFAULT_EXECUTIONS
