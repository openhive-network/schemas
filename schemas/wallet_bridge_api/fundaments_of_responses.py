from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, HiveDateTime, HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class GetCollateralizedConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    requestid: HiveInt
    collateral_amount: AssetHive
    converted_amount: AssetHbd
    conversion_date: HiveDateTime


class GetConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="field")
    owner: AccountName
    requestid: HiveInt
    amount: AssetHbd
    conversion_date: HiveDateTime
