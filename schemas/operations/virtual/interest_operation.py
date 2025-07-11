from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_IS_SAVED_INTO_HBD_BALANCE: Final[bool] = False


class InterestOperation(VirtualOperation, kw_only=True):
    owner: AccountName
    interest: AssetHbd
    is_saved_into_hbd_balance: bool = DEFAULT_IS_SAVED_INTO_HBD_BALANCE

    @classmethod
    def get_name(cls) -> str:
        return "interest"

    @classmethod
    def vop_offset(cls) -> int:
        return 5
