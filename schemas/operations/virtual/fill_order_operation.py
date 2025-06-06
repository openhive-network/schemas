from __future__ import annotations

from typing import Final

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.virtual_operation import VirtualOperation

DEFAULT_CURRENT_ORDERID: Final[Uint32t] = Uint32t(0)
DEFAULT_OPEN_ORDERID: Final[Uint32t] = Uint32t(0)


class FillOrderOperation(VirtualOperation, kw_only=True):
    current_owner: AccountName
    current_orderid: Uint32t = DEFAULT_CURRENT_ORDERID
    current_pays: AssetUnionAssetHiveAssetHbd
    open_owner: AccountName
    open_orderid: Uint32t = DEFAULT_OPEN_ORDERID
    open_pays: AssetUnionAssetHiveAssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "fill_order"

    @classmethod
    def vop_offset(cls) -> int:
        return 7
