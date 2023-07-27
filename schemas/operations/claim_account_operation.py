from __future__ import annotations

from typing import Generic, Literal

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHive
from schemas.preconfigured_base_model import Operation

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class ClaimAccountOperation(Generic[AssetHive], GenericModel, Operation):
    creator: AccountName
    fee: AssetHive | Literal[0]