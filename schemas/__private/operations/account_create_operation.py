from __future__ import annotations

from typing import Any

from pydantic import Json

from schemas.__private.hive_fields_schemas_strict import (
    AccountName,
    AssetHive,
    Authority,
    EmptyString,
    PublicKey,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AccountCreateOperation(PreconfiguredBaseModel):
    fee: AssetHive
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json[Any] | EmptyString
