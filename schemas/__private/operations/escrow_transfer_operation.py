from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas_strict import Uint32t
from schemas.__private.operations_strict.escrow_transfer_operation_strict import EscrowTransferOperationStrict

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowTransferOperation(EscrowTransferOperationStrict):
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
