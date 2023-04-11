from schemas.package.schemas.predefined import AccountName, Uint16t
from preconfigure_base_model import PreconfiguredBaseModel


class CustomOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    id: Uint16t = 0
    data: list[str]
    