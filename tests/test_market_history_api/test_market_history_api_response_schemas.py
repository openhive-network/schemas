from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.market_history_api.response_schemas import (
    GetMarketHistory,
    GetMarketHistoryBuckets,
    GetRecentTrades,
    GetTicker,
    GetTradeHistory,
    GetVolume,
)
from schemas.jsonrpc import get_response_model

from .response_schemas import (
    GET_MARKET_HISTORY,
    GET_MARKET_HISTORY_BUCKETS,
    GET_RECENT_TRADES,
    GET_TICKER,
    GET_TRADE_HISTORY,
    GET_VOLUME,
)


@pytest.mark.parametrize(
    "schema, parameters, endpoint",
    [
        (GetMarketHistory, GET_MARKET_HISTORY, "market_history_api.get_market_history"),
        (GetVolume, GET_VOLUME, "market_history_api.get_volume"),
        (GetTicker, GET_TICKER, "market_history_api.get_ticker"),
        (GetMarketHistoryBuckets, GET_MARKET_HISTORY_BUCKETS, "market_history_api.get_market_history_buckets"),
        (GetTradeHistory, GET_TRADE_HISTORY, "market_history_api.get_trade_history"),
        (GetRecentTrades, GET_RECENT_TRADES, "market_history_api.get_recent_trades"),
    ],
)
def test_market_history_api_responses_correct_values(schema: Any, parameters: dict[str, Any], endpoint: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, endpoint, **parameters)
