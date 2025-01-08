from __future__ import annotations

from typing import Any, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Int64t
from schemas.operation import Operation


class _UpdateProposalOperation(Operation):
    __operation_name__ = "update_proposal"
    __offset__ = 47

    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: list[Any] = Field(default_factory=list)


class UpdateProposalOperation(_UpdateProposalOperation):
    ...


class UpdateProposalOperationLegacy(_UpdateProposalOperation):
    ...
