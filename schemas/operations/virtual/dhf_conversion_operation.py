from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel


class _DhfConversionOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "dhf_conversion"
    __offset__ = 24

    treasury: AccountName
    hive_amount_in: AssetHiveT
    hbd_amount_out: AssetHbdT


class DhfConversionOperation(_DhfConversionOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class DhfConversionOperationLegacy(_DhfConversionOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
