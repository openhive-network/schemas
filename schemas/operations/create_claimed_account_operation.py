from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, Authority, PublicKey
from schemas.preconfigured_base_model import Operation


class CreateClaimedAccountOperation(Operation):
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
