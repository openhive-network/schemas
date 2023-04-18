from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.operations_strict.transfer_to_vesting_operation_strict import TransferToVestingOperationStrict

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName


class TransferToVestingOperation(TransferToVestingOperationStrict):
    to: AccountName | None = None
