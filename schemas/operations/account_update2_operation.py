from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority, PublicKey
from schemas.operation import Operation


class AccountUpdate2Operation(Operation):
    __operation_name__ = "account_update2"

    account: AccountName
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey | None = None
    json_metadata: str
    posting_json_metadata: str
