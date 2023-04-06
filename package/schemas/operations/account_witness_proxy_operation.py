from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName


class AccountWitnessProxyOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    proxy: AccountName  # should be HIVE_PROXY_TO_SELF_ACCOUNT ???
