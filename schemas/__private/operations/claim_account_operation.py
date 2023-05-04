from __future__ import annotations

from typing import Generic, Literal

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import AccountName, AssetHive
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class ClaimAccountOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    creator: AccountName
    fee: AssetHive | Literal[0]
