from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority, PublicKey
from schemas.__private.operation import Operation


class AccountUpdateOperation(Operation):
    __operation_name__ = "account_update"

    account: AccountName
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey
    json_metadata: str
