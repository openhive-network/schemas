from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.operations_strict.account_update_operation_strict import AccountUpdateOperationStrict

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import Authority


class AccountUpdateOperation(AccountUpdateOperationStrict):
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
