from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from pydantic import Json

    from schemas.__private.hive_fields_schemas import AccountName, Authority, PublicKey


class CreateClaimedAccountOperation(PreconfiguredBaseModel):
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json
