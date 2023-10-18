from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hex import TransactionId
from schemas.fields.integers import Uint16t, Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_OP_IN_TRX: Final[Uint16t] = Uint16t(0)


class _ProposalPayOperation(VirtualOperation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "proposal_pay"
    __offset__ = 16

    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    receiver: AccountName
    payer: AccountName
    payment: AssetHbdT
    trx_id: TransactionId
    op_in_trx: Uint16t = DEFAULT_OP_IN_TRX


class ProposalPayOperation(_ProposalPayOperation[AssetHbdHF26]):
    ...


class ProposalPayOperationLegacy(_ProposalPayOperation[AssetHbdLegacy]):
    ...
