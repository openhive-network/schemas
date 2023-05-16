from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    HiveDateTime,
    Int64t,
)
from schemas.__private.preconfigured_base_model import Operation


class UpdateProposalOperation(Operation, GenericModel, Generic[AssetHbd]):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
