from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import Authority
from schemas.__private.operations_strict.account_update_operation_strict import AccountUpdateOperationStrict


class AccountUpdateOperation(AccountUpdateOperationStrict):
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
