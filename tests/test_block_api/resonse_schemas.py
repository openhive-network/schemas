from __future__ import annotations

from typing import Any, Final

GET_BLOCK: Final[dict[str, Any]] = {
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "block": {
            "previous": "0000000000000000000000000000000000000000",
            "timestamp": "2016-03-24T16:05:00",
            "witness": "initminer",
            "transaction_merkle_root": "0000000000000000000000000000000000000000",
            "extensions": [],
            "witness_signature": "204f8ad56a8f5cf722a02b035a61b500aa59b9519b2c33c77a80c0a714680a5a5a7a340d909d19996613c5e4ae92146b9add8a7a663eef37d837ef881477313043",
            "transactions": [],
            "block_id": "0000000109833ce528d5bbfb3f6225b39ee10086",
            "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
            "transaction_ids": [],
        }
    },
}


GET_BLOCK_HEADER: Final[dict[str, Any]] = {
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "header": {
            "previous": "0000000000000000000000000000000000000000",
            "timestamp": "2016-03-24T16:05:00",
            "witness": "initminer",
            "transaction_merkle_root": "0000000000000000000000000000000000000000",
            "extensions": [],
        }
    },
}


GET_BLOCK_RANGE: Final[dict[str, Any]] = {
    "jsonrpc": "2.0",
    "result": {
        "blocks": [
            {
                "previous": "0000000000000000000000000000000000000000",
                "timestamp": "2016-03-24T16:05:00",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "204f8ad56a8f5cf722a02b035a61b500aa59b9519b2c33c77a80c0a714680a5a5a7a340d909d19996613c5e4ae92146b9add8a7a663eef37d837ef881477313043",
                "transactions": [],
                "block_id": "0000000109833ce528d5bbfb3f6225b39ee10086",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "0000000109833ce528d5bbfb3f6225b39ee10086",
                "timestamp": "2016-03-24T16:05:36",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "1f3e85ab301a600f391f11e859240f090a9404f8ebf0bf98df58eb17f455156e2d16e1dcfc621acb3a7acbedc86b6d2560fdd87ce5709e80fa333a2bbb92966df3",
                "transactions": [],
                "block_id": "00000002ed04e3c3def0238f693931ee7eebbdf1",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "00000002ed04e3c3def0238f693931ee7eebbdf1",
                "timestamp": "2016-03-24T16:05:39",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "205ad1d3f0d42abcfdacb179de1acecf873be432cc546dde6b35184d261868b47b17dc1717b78a1572843fdd71a654e057db03f2df5d846b71606ec80455a199a6",
                "transactions": [],
                "block_id": "000000035b094a812646289c622dba0ba67d1ffe",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "000000035b094a812646289c622dba0ba67d1ffe",
                "timestamp": "2016-03-24T16:05:42",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "202c7e5cada5104170365a83734a229eac0e427af5ed03fe2268e79bb9b05903d55cb96547987b57cd1ba5ed1a5ae1a9372f0ee6becfd871c2fcc26dc8b057149e",
                "transactions": [],
                "block_id": "00000004f9de0cfeb08c9d7d9d1fe536d902dc4a",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "00000004f9de0cfeb08c9d7d9d1fe536d902dc4a",
                "timestamp": "2016-03-24T16:05:45",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "1f508f1124db7f1442946b5e3b3a5f822812e54e18dffcda83385a9664b825d27214f0cdd0a0a7e7aeb6467f428fbc291c6f64b60da29e8ad182c20daf71b68b8b",
                "transactions": [],
                "block_id": "00000005014b5562a1133070d8bee536de615329",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "00000005014b5562a1133070d8bee536de615329",
                "timestamp": "2016-03-24T16:05:48",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "1f6bcfe700cc88f5c91fbc82fdd46623fed31c95071dbfedafa9faaad76ac788527658fb11ae57a602feac3d8a5b8d2ec4c47ef361b9f64d5b9db267642fc78bc3",
                "transactions": [],
                "block_id": "00000006e323e35687e160b8aec86f1e56d4c902",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "00000006e323e35687e160b8aec86f1e56d4c902",
                "timestamp": "2016-03-24T16:05:51",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "1f5202b4570f1b0d8b197a5f5729389e762ca7e6b74d179d54c51cf4f79694eb130c2cc39d31fa29e2d54dc9aa9fab83fedba981d415e0b341f0040183e2d1997c",
                "transactions": [],
                "block_id": "000000079ff02a2dea6c4d9a27f752233d4a66b4",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "000000079ff02a2dea6c4d9a27f752233d4a66b4",
                "timestamp": "2016-03-24T16:05:54",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "2050e555bd40af001737ccebc03d4b6e104eaa9f46f1acac03f9d4dd1b7af3cf1c45c6e232364fda7f6c72ff2942d0a35d148ee4b6ba52332c11c3b528cd01d8c3",
                "transactions": [],
                "block_id": "000000084f957cc170a27c8330293a3343f82c23",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "000000084f957cc170a27c8330293a3343f82c23",
                "timestamp": "2016-03-24T16:05:57",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "2044cd87f6f0a98b37c520b61349de4b36ab82aa8cc799c7ce0f14635ae2a266b02412af616deecba6cda06bc1f3823b2abd252cfe592643920e67ccdc73aef6f9",
                "transactions": [],
                "block_id": "00000009f35198cfd8a866868538bed3482d61a4",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
            {
                "previous": "00000009f35198cfd8a866868538bed3482d61a4",
                "timestamp": "2016-03-24T16:06:00",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "1f6ac53a8bb6ca885e988baafb1363b98e8807f62e6256462269b7288c568010096402d9bd2d8a69549568477f79570e8a41474daee2b7d29c623a0b5649081417",
                "transactions": [],
                "block_id": "0000000aae44a2f4d57170dab16fb1619f9e1d0e",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            },
        ]
    },
    "id": 1,
}
