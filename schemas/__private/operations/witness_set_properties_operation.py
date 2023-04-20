from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.hive_fields_schemas_strict import LegacyChainPropertiesStrict
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WitnessSetPropertiesOperation(PreconfiguredBaseModel):
    witness: AccountName
    props: LegacyChainPropertiesStrict