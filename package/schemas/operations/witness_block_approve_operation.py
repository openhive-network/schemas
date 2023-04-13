from schemas.__private.hive_fields_schemas import AccountName, Uint32t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class WitnessBlockApproveOperation(PreconfiguredBaseModel):
    witness: AccountName
    block_id: Uint32t
