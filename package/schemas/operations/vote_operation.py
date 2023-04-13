from schemas.__private.hive_fields_schemas import AccountName, Int16t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class VoteOperation(PreconfiguredBaseModel):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Int16t = 0
