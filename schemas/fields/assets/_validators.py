from __future__ import annotations

from typing import Any

from schemas.fields.assets.asset_info import AssetInfo


def validate_nai(value: Any, asset_info: AssetInfo) -> Any:
    if value != asset_info.nai:
        raise ValueError("Invalid nai !")
    return value


def validate_precision(value: int, asset_info: AssetInfo) -> int:
    if value != asset_info.precision:
        raise ValueError("Invalid decimals")
    return value
