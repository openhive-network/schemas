from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = 0


class ProposalPayOperation(VirtualOperation, kw_only=True):
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    receiver: AccountName
    payer: AccountName
    payment: AssetHbd
    conversion: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "proposal_pay"

    @classmethod
    def vop_offset(cls) -> int:
        return 16
