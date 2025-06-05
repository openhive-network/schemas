from __future__ import annotations

from typing import Any

from msgspec import field

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Int64t
from schemas.operation import Operation


class _UpdateProposalOperation(Operation):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: list[Any] = field(default_factory=list)

    @classmethod
    def get_name(cls) -> str:
        return "update_proposal"

    @classmethod
    def offset(cls) -> int:
        return 47


class UpdateProposalOperation(_UpdateProposalOperation):
    ...


class UpdateProposalOperationLegacy(_UpdateProposalOperation):
    ...
