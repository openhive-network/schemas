from schemas.package.schemas.predefined import AccountName, Int64t
from preconfigure_base_model import PreconfiguredBaseModel


class RemoveProposalOperation(PreconfiguredBaseModel):
    proposal_owner: AccountName
    proposal_ids: list[Int64t]
