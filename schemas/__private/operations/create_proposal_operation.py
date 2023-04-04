from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, HiveDateTime
from schemas.__private.preconfigured_base_model import Operation


class CreateProposalOperation(Generic[AssetHbd], GenericModel, Operation):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
