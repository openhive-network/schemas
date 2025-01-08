from __future__ import annotations


from schemas.fields.basic import AccountName
from schemas.fields.compound import HbdExchangeRate
from schemas.operation import Operation


class FeedPublishOperation(Operation):
    __operation_name__ = "feed_publish"
    __offset__ = 7

    publisher: AccountName
    exchange_rate: HbdExchangeRate
