from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority, PublicKey
from schemas.operation import Operation


class CreateClaimedAccountOperation(Operation):
    __operation_name__ = "create_claimed_account"

    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
