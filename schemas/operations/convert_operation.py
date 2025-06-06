from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class ConvertOperation(Operation, kw_only=True):
    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "convert"

    @classmethod
    def offset(cls) -> int:
        return 8
