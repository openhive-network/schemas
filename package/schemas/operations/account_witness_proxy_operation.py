from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName


class AccountWitnessProxyOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    proxy: str  # should be HIVE_PROXY_TO_SELF_ACCOUNT ???
