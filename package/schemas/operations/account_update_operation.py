from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from pydantic import Json

    from schemas.__private.hive_fields_schemas import AccountName, Authority, PublicKey


class AccountUpdateOperation(PreconfiguredBaseModel):
    account: AccountName
    owner: Authority | None
    active: Authority | None
    posting: Authority | None
    memo_key: PublicKey
    json_metadata: Json
