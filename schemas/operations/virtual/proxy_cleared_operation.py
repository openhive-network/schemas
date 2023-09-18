from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ProxyClearedOperation(VirtualOperation):
    __operation_name__ = "proxy_cleared"

    account: AccountName
    proxy: AccountName
