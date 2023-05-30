from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive
from schemas.__private.preconfigured_base_model import VirtualOperation


class DhfConversionOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    treasury: AccountName
    hive_amount_in: AssetHive
    hbd_amount_out: AssetHbd
