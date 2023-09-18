from __future__ import annotations

from schemas.fields.basic import AccountName, AssetHiveHF26, LegacyChainProperties
from schemas.operation import Operation


class WitnessSetPropertiesOperation(Operation):
    __operation_name__ = "witness_set_properties"

    witness: AccountName
    props: LegacyChainProperties[AssetHiveHF26]
