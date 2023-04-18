from __future__ import annotations

from typing import TYPE_CHECKING, Any

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from pydantic import Json

    from schemas.__private.hive_fields_schemas import AccountName, AssetHive, AssetHiveLegacy, Authority, PublicKey


class AccountCreateOperation(PreconfiguredBaseModel):
    fee: AssetHive | AssetHiveLegacy
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json[Any]
