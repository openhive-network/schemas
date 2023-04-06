from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, HbdExchangeRateLegacyFalse, HbdExchangeRateLegacyTrue


class FeedPublishOperation(BaseModel):
    publisher: AccountName
    exchange_rate: HbdExchangeRateLegacyFalse | HbdExchangeRateLegacyTrue
