from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, AssetHive, LegacyAssetHive

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class ClaimAccountOperation(PreconfiguredBaseModel):
    creator: AccountName
    fee: AssetHive | LegacyAssetHive | Literal[0]
