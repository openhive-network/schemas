from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.operations_strict.account_update2_operation_strict import AccountUpdate2OperationStrict

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import Authority, PublicKey


class AccountUpdate2Operation(AccountUpdate2OperationStrict):
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey | None = None
