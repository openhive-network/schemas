from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import Uint32t
from schemas.__private.operations_strict.escrow_approve_operation_strict import EscrowApproveOperationStrict

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)
DEFAULT_APPROVE: Final[bool] = True


class EscrowApproveOperation(EscrowApproveOperationStrict):
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    approve: bool = DEFAULT_APPROVE
