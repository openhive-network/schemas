from __future__ import annotations

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class DhfFundingOperation(VirtualOperation, kw_only=True):
    treasury: AccountName
    additional_funds: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "dhf_funding"

    @classmethod
    def vop_offset(cls) -> int:
        return 17
