from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, HbdExchangeRate


class FeedPublishOperation(BaseModel, extra=Extra.forbid):
    publisher: AccountName
    exchange_rate: HbdExchangeRate
