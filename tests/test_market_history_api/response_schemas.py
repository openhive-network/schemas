from __future__ import annotations

from typing import Any, Final

GET_MARKET_HISTORY: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {
        "buckets": [
            {
                "id": 793307,
                "open": "2018-01-01T00:00:00",
                "seconds": 86400,
                "hive": {"high": 1, "low": 5, "open": 25650, "close": 1691, "volume": 111698586},
                "non_hive": {"high": 1, "low": 1, "open": 10192, "close": 801, "volume": 46183343},
            }
        ]
    },
    "id": 1,
}
GET_MARKET_HISTORY_BUCKETS: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {"bucket_sizes": [15, 60, 300, 3600, 86400]},
    "id": 1,
}
GET_RECENT_TRADES: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {
        "trades": [
            {
                "date": "2023-06-09T10:20:27",
                "current_pays": {"amount": "529184", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "174303", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:20:27",
                "current_pays": {"amount": "3385", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "1115", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:19:24",
                "current_pays": {"amount": "52", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "156", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:16:51",
                "current_pays": {"amount": "3000", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "9051", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:16:30",
                "current_pays": {"amount": "210200", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "69240", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:12:54",
                "current_pays": {"amount": "208875", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "68803", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:12:30",
                "current_pays": {"amount": "1231", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "3713", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:11:00",
                "current_pays": {"amount": "3032", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "999", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:08:24",
                "current_pays": {"amount": "181432", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "59763", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2023-06-09T10:08:12",
                "current_pays": {"amount": "201591", "precision": 3, "nai": "@@000000021"},
                "open_pays": {"amount": "66404", "precision": 3, "nai": "@@000000013"},
                "taker": "alice",
                "maker": "bob",
            },
        ]
    },
    "id": 1,
}
GET_TICKER: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {
        "latest": "0.32944732297063906",
        "lowest_ask": "0.33101506871998676",
        "highest_bid": "0.32939787485242028",
        "percent_change": "-2.41770293609671461",
        "hive_volume": {"amount": "126410336", "precision": 3, "nai": "@@000000021"},
        "hbd_volume": {"amount": "42151645", "precision": 3, "nai": "@@000000013"},
    },
    "id": 1,
}
GET_TRADE_HISTORY: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {
        "trades": [
            {
                "date": "2018-01-01T00:00:09",
                "current_pays": {"amount": "10192", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "25650", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:00:09",
                "current_pays": {"amount": "2000", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "5033", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:00:12",
                "current_pays": {"amount": "13560", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "34128", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:00:12",
                "current_pays": {"amount": "3057", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "7690", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:00:12",
                "current_pays": {"amount": "6908", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "17375", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:02:06",
                "current_pays": {"amount": "796", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "2000", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:05:03",
                "current_pays": {"amount": "296", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "742", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:05:09",
                "current_pays": {"amount": "16", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "40", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:07:48",
                "current_pays": {"amount": "582", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "1462", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
            {
                "date": "2018-01-01T00:07:48",
                "current_pays": {"amount": "1992", "precision": 3, "nai": "@@000000013"},
                "open_pays": {"amount": "5000", "precision": 3, "nai": "@@000000021"},
                "taker": "alice",
                "maker": "bob",
            },
        ]
    },
    "id": 1,
}
GET_VOLUME: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {
        "hive_volume": {"amount": "119698620", "precision": 3, "nai": "@@000000021"},
        "hbd_volume": {"amount": "39885679", "precision": 3, "nai": "@@000000013"},
    },
    "id": 1,
}
