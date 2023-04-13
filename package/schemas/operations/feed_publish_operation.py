from schemas.__private.hive_fields_schemas import AccountName, HbdExchangeRate
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class FeedPublishOperation(PreconfiguredBaseModel):
    publisher: AccountName
    exchange_rate: HbdExchangeRate
