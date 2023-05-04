from __future__ import annotations

from schemas.__private.hive_fields_schemas import AssetHbdNai, AssetHiveNai
from schemas.__private.hive_fields_schemas import HbdExchangeRate as HbdExchangeRateGeneric
from schemas.__private.hive_fields_schemas import LegacyChainProperties as LegacyChainPropertiesGeneric

HbdExchangeRate = HbdExchangeRateGeneric[AssetHbdNai, AssetHiveNai]
LegacyChainProperties = LegacyChainPropertiesGeneric[AssetHiveNai]

__all__ = ["HbdExchangeRate", "LegacyChainProperties"]
