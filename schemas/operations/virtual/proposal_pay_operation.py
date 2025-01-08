from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class _ProposalPayOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "proposal_pay"
    __offset__ = 16

    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    receiver: AccountName
    payer: AccountName
    payment: AssetHbd


class ProposalPayOperation(_ProposalPayOperation):
    ...


class ProposalPayOperationLegacy(_ProposalPayOperation):
    ...
