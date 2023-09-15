from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, Uint32t
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class ProposalFeeOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    creator: AccountName
    treasury: AccountName
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    fee: AssetHbd
