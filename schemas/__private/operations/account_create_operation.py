from __future__ import annotations

from typing import Any, Generic

from pydantic import Json
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import AccountName, AssetHive, Authority, EmptyString, PublicKey
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AccountCreateOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    fee: AssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json[Any] | EmptyString
