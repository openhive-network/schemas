from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, AssetHiveHF26, LegacyChainProperties
from schemas.preconfigured_base_model import Operation


class WitnessSetPropertiesOperation(Operation):
    witness: AccountName
    props: LegacyChainProperties[AssetHiveHF26]
