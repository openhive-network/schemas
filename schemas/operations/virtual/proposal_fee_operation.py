from __future__ import annotations

from typing import Final, Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel

DEFAULT_PROPOSAL_ID: Final[Uint32t] = Uint32t(0)


class _ProposalFeeOperation(VirtualOperation, BaseModel, Generic[AssetHbdT]):
    __operation_name__ = "proposal_fee"
    __offset__ = 37

    creator: AccountName
    treasury: AccountName
    proposal_id: Uint32t = DEFAULT_PROPOSAL_ID
    fee: AssetHbdT


class ProposalFeeOperation(_ProposalFeeOperation[AssetHbdHF26]):
    ...


class ProposalFeeOperationLegacy(_ProposalFeeOperation[AssetHbdLegacy]):
    ...
