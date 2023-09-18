from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
    Int64t,
)
from schemas.operation import Operation


class _UpdateProposalOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "update_proposal"

    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbdT
    subject: str
    permlink: str
    extensions: list[Any] | None


class UpdateProposalOperation(_UpdateProposalOperation[AssetHbdHF26]):
    ...


class UpdateProposalOperationLegacy(_UpdateProposalOperation[AssetHbdLegacy]):
    ...
