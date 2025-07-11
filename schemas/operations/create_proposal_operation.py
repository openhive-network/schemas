from __future__ import annotations

from msgspec import field

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class CreateProposalOperation(Operation):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: FutureExtensions = field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls) -> str:
        return "create_proposal"

    @classmethod
    def offset(cls) -> int:
        return 44
