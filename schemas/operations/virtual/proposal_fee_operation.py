from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class _ProposalFeeOperation(VirtualOperation, kw_only=True):
    creator: AccountName
    treasury: AccountName
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    fee: AssetHbd


    @classmethod
    def get_name(cls):
        return "proposal_fee"
    
    @classmethod
    def offset(cls):
        return 37

class ProposalFeeOperation(_ProposalFeeOperation):
    ...


class ProposalFeeOperationLegacy(_ProposalFeeOperation):
    ...
