from __future__ import annotations

from typing import Any

from pydantic import Json

from schemas.__private.hive_fields_schemas import AccountName, Authority, EmptyString, PublicKey
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AccountUpdate2Operation(PreconfiguredBaseModel):
    account: AccountName
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey | None = None
    json_metadata: Json[Any] | EmptyString
    posting_json_metadata: Json[Any] | EmptyString
