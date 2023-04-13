from schemas.__private.hive_fields_schemas import AccountName, LegacyChainProperties
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class WitnessSetPropertiesOperation(PreconfiguredBaseModel):
    witness: AccountName
    props: LegacyChainProperties
