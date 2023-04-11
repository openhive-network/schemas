from schemas.package.schemas.predefined import AccountName, HbdExchangeRate
from preconfigure_base_model import PreconfiguredBaseModel


class FeedPublishOperation(PreconfiguredBaseModel):
    publisher: AccountName
    exchange_rate: HbdExchangeRate
