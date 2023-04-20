"""
    Strict versions of fields are using just for checking poles from api response. In this situation it is undeliverable
    to include default values to some poles like for example nai in NaiAssets, situation like that would lead to
    situation when nai field is empty in response from api and for pydantic it would be okay due to defaults
"""
from __future__ import annotations

from typing import TypeAlias

from schemas.__private.hive_constants import HBD_INTEREST_RATE, MAXIMUM_BLOCK_SIZE
from schemas.__private.hive_fields_schemas import (
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetNai,
    AssetVestsLegacy,
    Uint16t,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AssetHiveNaiStrict(AssetNai):
    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000021"


class AssetHbdNaiStrict(AssetNai):
    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000013"


class AssetVestsNaiStrict(AssetNai):
    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000037"


"""Assets to use just in situation when it doesn't matter that Assets must be in nai or legacy format"""
AssetHbdStrict: TypeAlias = AssetHbdNaiStrict | AssetHbdLegacy
AssetHiveStrict: TypeAlias = AssetHiveNaiStrict | AssetHiveLegacy
AssetVestsStrict: TypeAlias = AssetVestsNaiStrict | AssetVestsLegacy


class HbdExchangeRateStrict(PreconfiguredBaseModel):
    base: AssetHiveStrict | AssetHbdStrict
    quote: AssetHiveStrict


class LegacyChainPropertiesStrict(PreconfiguredBaseModel):
    account_creation_fee: AssetHiveStrict
    maximum_block_size: Uint32t = Uint32t(MAXIMUM_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HBD_INTEREST_RATE)
