from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _DhfConversionOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "dhf_conversion"
    __offset__ = 24

    treasury: AccountName
    hive_amount_in: AssetHive
    hbd_amount_out: AssetHbd


class DhfConversionOperation(_DhfConversionOperation):
    ...


class DhfConversionOperationLegacy(_DhfConversionOperation):
    ...
