from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _DhfConversionOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "dhf_conversion"

    treasury: AccountName
    hive_amount_in: AssetHive
    hbd_amount_out: AssetHbd


class DhfConversionOperation(_DhfConversionOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class DhfConversionOperationLegacy(_DhfConversionOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
