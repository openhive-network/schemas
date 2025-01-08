from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel


from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.virtual_operation import VirtualOperation


class _ClearNullAccountBalanceOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "clear_null_account_balance"
    __offset__ = 15

    total_cleared: list[AssetHive | AssetHbd | AssetVest]


class ClearNullAccountBalanceOperation(_ClearNullAccountBalanceOperation):
    ...


class ClearNullAccountBalanceOperationLegacy(
    _ClearNullAccountBalanceOperation
):
    ...
