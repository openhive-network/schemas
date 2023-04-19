from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.operations_strict.transfer_to_vesting_operation_strict import TransferToVestingOperationStrict


class TransferToVestingOperation(TransferToVestingOperationStrict):
    to: AccountName | None = None
