from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation


class _CreateProposalOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "create_proposal"

    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbdT
    subject: str
    permlink: str


class CreateProposalOperation(_CreateProposalOperation[AssetHbdHF26]):
    ...


class CreateProposalOperationLegacy(_CreateProposalOperation[AssetHbdLegacy]):
    ...
