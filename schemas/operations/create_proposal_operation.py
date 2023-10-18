from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class _CreateProposalOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "create_proposal"
    __offset__ = 44

    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbdT
    subject: str
    permlink: str
    extensions: FutureExtensions


class CreateProposalOperation(_CreateProposalOperation[AssetHbdHF26]):
    ...


class CreateProposalOperationLegacy(_CreateProposalOperation[AssetHbdLegacy]):
    ...
