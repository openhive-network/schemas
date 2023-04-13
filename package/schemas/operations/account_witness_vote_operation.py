from schemas.__private.hive_fields_schemas import AccountName
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class AccountWitnessVoteOperation(PreconfiguredBaseModel):
    account: AccountName
    witness: AccountName
    approve: bool = True
