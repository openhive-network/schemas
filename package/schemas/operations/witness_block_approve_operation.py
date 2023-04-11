from schemas.package.schemas.predefined import AccountName, Uint32t
from preconfigure_base_model import PreconfiguredBaseModel


class WitnessBlockApproveOperation(PreconfiguredBaseModel):
    witness: AccountName
    block_id: Uint32t
