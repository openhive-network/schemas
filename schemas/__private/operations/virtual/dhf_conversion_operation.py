from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive
from schemas.__private.virtual_operation import VirtualOperation


class DhfConversionOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    treasury: AccountName
    hive_amount_in: AssetHive
    hbd_amount_out: AssetHbd
