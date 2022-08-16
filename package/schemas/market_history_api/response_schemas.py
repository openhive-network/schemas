from schemas.predefined import *

get_market_history = Map({
    'buckets': Array(
        Map({
            'id': Int(),
            'open': Date(),
            'seconds': Int(),
            'hive': Map({
                'high': Int(),
                'low': Int(),
                'open': Int(),
                'close': Int(),
                'volume': Int(),
            }),
            'non_hive': Map({
                'high': Int(),
                'low': Int(),
                'open': Int(),
                'close': Int(),
                'volume': Int(),
            }),
        })
    )
})

get_market_history_buckets = Map({
    'bucket_sizes': Array(enum=[[15, 60, 300, 3600, 86400]])
})

get_order_book = Map({
    'asks': Array(Map({
        'created': Date(),
        'hbd': Int(),
        'hive': Int(),
        'order_price': Price(AssetAny(), AssetAny()),
        'real_price': Str(),
        })
    ),
    'bids': Array(Map({
        'created': Date(),
        'hbd': Int(),
        'hive': Int(),
        'order_price': Price(AssetAny(), AssetAny()),
        'real_price': Str()
        })
    ),
})


get_recent_trades = Map({
    'trades': Array(
        Map({
            'date': Date(),
            'current_pays': AnyOf(AssetHive(), AssetHbd()),
            'open_pays': AnyOf(AssetHive(), AssetHbd()),
        })
    )
})

get_ticker = Map({
    'latest': Str(),
    'lowest_ask': Str(),
    'highest_bid': Str(),
    'percent_change': Str(),
    'hive_volume': AssetHive(),
    'hbd_volume': AssetHbd(),
})

get_trade_history = Map({
    'trades': Array(
        Map({
            'date': Date(),
            'current_pays': AnyOf(AssetHive(), AssetHbd()),
            'open_pays': AnyOf(AssetHive(), AssetHbd()),
        })
    )
})

get_volume = Map({
    'hive_volume': AssetHive(),
    'hbd_volume': AssetHbd(),
})
