from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas_strict import Uint32t
from schemas.__private.operations_strict.escrow_dispute_operation_strict import EscrowDisputeOperationStrict

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowDisputeOperation(EscrowDisputeOperationStrict):
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
