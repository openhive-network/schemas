from schemas.package.schemas.predefined import AccountName, Int16t
from preconfigure_base_model import PreconfiguredBaseModel


class VoteOperation(PreconfiguredBaseModel):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Int16t = 0
