from __future__ import annotations

import json
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
    "schema, parameters",
    [
        (GetMarketHistory, GET_MARKET_HISTORY),
        (GetVolume, GET_VOLUME),
        (GetTicker, GET_TICKER),
        (GetMarketHistoryBuckets, GET_MARKET_HISTORY_BUCKETS),
        (GetTradeHistory, GET_TRADE_HISTORY),
        (GetRecentTrades, GET_RECENT_TRADES),
    ],
)
def test_market_history_api_responses_correct_values(schema: Any, parameters: dict[str, Any]) -> None:
    # ACT & ASSERT
    get_response_model(schema, json.dumps(parameters))
