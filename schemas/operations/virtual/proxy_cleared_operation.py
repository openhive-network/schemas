from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ProxyClearedOperation(VirtualOperation):
    account: AccountName
    proxy: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "proxy_cleared"

    @classmethod
    def vop_offset(cls) -> int:
        return 41
