from schemas.package.schemas.predefined import AccountName, LegacyChainProperties
from preconfigure_base_model import PreconfiguredBaseModel


class WitnessSetPropertiesOperation(PreconfiguredBaseModel):
    witness: AccountName
    props: LegacyChainProperties
