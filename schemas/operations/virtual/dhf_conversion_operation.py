from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
)
from schemas.virtual_operation import VirtualOperation


class _DhfConversionOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "dhf_conversion"

    treasury: AccountName
    hive_amount_in: AssetHiveT
    hbd_amount_out: AssetHbdT


class DhfConversionOperation(_DhfConversionOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class DhfConversionOperationLegacy(_DhfConversionOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
