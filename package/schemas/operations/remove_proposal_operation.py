from schemas.__private.hive_fields_schemas import AccountName, Int64t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class RemoveProposalOperation(PreconfiguredBaseModel):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
