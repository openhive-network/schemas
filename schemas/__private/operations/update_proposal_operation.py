from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    HiveDateTime,
    Int64t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class UpdateProposalOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
