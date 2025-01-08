from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class _CreateProposalOperation(Operation):
    __operation_name__ = "create_proposal"
    __offset__ = 44

    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)


class CreateProposalOperation(_CreateProposalOperation):
    ...


class CreateProposalOperationLegacy(_CreateProposalOperation):
    ...
