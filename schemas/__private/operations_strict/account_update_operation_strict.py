from __future__ import annotations

from typing import Any

from pydantic import Json

from schemas.__private.hive_fields_schemas import AccountName, Authority, EmptyString, PublicKey
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AccountUpdateOperationStrict(PreconfiguredBaseModel):
    account: AccountName
    owner: Authority | None
    active: Authority | None
    posting: Authority | None
    memo_key: PublicKey
    json_metadata: Json[Any] | EmptyString
