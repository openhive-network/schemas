from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, AssetHiveNai, LegacyChainProperties
from schemas.__private.preconfigured_base_model import Operation


class WitnessSetPropertiesOperation(Operation):
    witness: AccountName
    props: LegacyChainProperties[AssetHiveNai]
