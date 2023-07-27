from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd, Uint16t, Uint32t
from schemas.hive_fields_custom_schemas import TransactionId
from schemas.preconfigured_base_model import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_OP_IN_TRX: Final[Uint16t] = Uint16t(0)


class ProposalPayOperation(Generic[AssetHbd], GenericModel, VirtualOperation):
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    receiver: AccountName
    payer: AccountName
    payment: AssetHbd
    trx_id: TransactionId
    op_in_trx: Uint16t = DEFAULT_OP_IN_TRX
