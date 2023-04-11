from schemas.package.schemas.predefined import AccountName
from preconfigure_base_model import PreconfiguredBaseModel


class AccountWitnessVoteOperation(PreconfiguredBaseModel):
    account: AccountName
    witness: AccountName
    approve: bool = True
