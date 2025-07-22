from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = 0


class ProposalFeeOperation(VirtualOperation, kw_only=True):
    creator: AccountName
    treasury: AccountName
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    fee: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "proposal_fee"

    @classmethod
    def vop_offset(cls) -> int:
        return 37
