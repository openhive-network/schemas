from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHive, Authority, PublicKey
from schemas.preconfigured_base_model import Operation


class AccountCreateOperation(Generic[AssetHive], GenericModel, Operation):
    fee: AssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
