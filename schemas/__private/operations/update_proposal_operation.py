from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    Int64t,
)
from schemas.__private.operation import Operation


class UpdateProposalOperation(Operation, GenericModel, Generic[AssetHbd]):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: list[Any] | None
