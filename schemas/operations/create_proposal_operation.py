from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation


class _CreateProposalOperation(Operation, GenericModel, Generic[AssetHbd]):
    __operation_name__ = "create_proposal"

    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str


class CreateProposalOperation(_CreateProposalOperation[AssetHbdHF26]):
    ...


class CreateProposalOperationLegacy(_CreateProposalOperation[AssetHbdLegacy]):
    ...