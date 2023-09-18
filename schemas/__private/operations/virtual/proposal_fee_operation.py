from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHbdHF26, AssetHbdLegacy, Uint32t
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class _ProposalFeeOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    __operation_name__ = "proposal_fee"

    creator: AccountName
    treasury: AccountName
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    fee: AssetHbd


class ProposalFeeOperation(_ProposalFeeOperation[AssetHbdHF26]):
    ...


class ProposalFeeOperationLegacy(_ProposalFeeOperation[AssetHbdLegacy]):
    ...
