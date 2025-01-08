from __future__ import annotations

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _DhfConversionOperation(VirtualOperation, kw_only=True):
    treasury: AccountName
    hive_amount_in: AssetHive
    hbd_amount_out: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "dhf_conversion"

    @classmethod
    def offset(cls) -> int:
        return 924


class DhfConversionOperation(_DhfConversionOperation):
    ...


class DhfConversionOperationLegacy(_DhfConversionOperation):
    ...
