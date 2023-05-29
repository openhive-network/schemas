from __future__ import annotations

from pydantic import validator

from schemas.__private.hive_fields_basic_schemas import HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.transaction_status_api.fundaments_of_responses import TransactionStatus


class FindTransaction(PreconfiguredBaseModel):
    block_num: HiveInt | None
    status: str

    @validator("status")
    @classmethod
    def check_status(cls, value: str) -> str:
        if value not in TransactionStatus.list_values():
            raise ValueError("This status type is incorrect")
        return value
