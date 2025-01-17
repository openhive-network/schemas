from __future__ import annotations

from typing import Final


from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class _ProposalPayOperation(VirtualOperation, kw_only=True):
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    receiver: AccountName
    payer: AccountName
    payment: AssetHbd


    @classmethod
    def get_name(cls):
        return "proposal_pay"
    
    @classmethod
    def offset(cls):
        return 16

class ProposalPayOperation(_ProposalPayOperation):
    ...


class ProposalPayOperationLegacy(_ProposalPayOperation):
    ...
