from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    Int64t,
)
from schemas.operation import Operation


class _UpdateProposalOperation(Operation, GenericModel, Generic[AssetHbd]):
    __operation_name__ = "update_proposal"

    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: list[Any] | None


class UpdateProposalOperation(_UpdateProposalOperation[AssetHbdHF26]):
    ...


class UpdateProposalOperationLegacy(_UpdateProposalOperation[AssetHbdLegacy]):
    ...
