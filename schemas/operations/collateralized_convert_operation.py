from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = 0


class CollateralizedConvertOperation(Operation, kw_only=True):
    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "collateralized_convert"

    @classmethod
    def offset(cls) -> int:
        return 48
