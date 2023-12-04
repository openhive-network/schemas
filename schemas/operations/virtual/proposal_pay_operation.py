from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class _ProposalPayOperation(VirtualOperation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "proposal_pay"
    __offset__ = 16

    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    receiver: AccountName
    payer: AccountName
    payment: AssetHbdT


class ProposalPayOperation(_ProposalPayOperation[AssetHbdHF26]):
    ...


class ProposalPayOperationLegacy(_ProposalPayOperation[AssetHbdLegacy]):
    ...
