from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.compound import HbdExchangeRate
from schemas.operation import Operation


class FeedPublishOperation(Operation):
    publisher: AccountName
    exchange_rate: HbdExchangeRate

    @classmethod
    def get_name(cls) -> str:
        return "feed_publish"

    @classmethod
    def offset(cls) -> int:
        return 7
