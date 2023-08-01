from __future__ import annotations

ENUM_VIRTUAL_OPS = {
    "jsonrpc": "2.0",
    "result": {
        "ops": [
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 1,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "miners",
                        "creator": "miners",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 2,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "null",
                        "creator": "null",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 1,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 3,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "temp",
                        "creator": "temp",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 2,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 4,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "initminer",
                        "creator": "initminer",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 3,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 5,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "steem",
                        "creator": "steem",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 4,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 1,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:05:00",
                "op": {
                    "type": "producer_reward_operation",
                    "value": {
                        "producer": "initminer",
                        "vesting_shares": {"amount": "1000000", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 5,
            },
        ],
        "ops_by_block": [],
        "next_block_range_begin": 2,
        "next_operation_begin": 0,
    },
    "id": 1,
}
GET_ACCOUNT_HISTORY = {
    "jsonrpc": "2.0",
    "result": {
        "history": [
            [
                998,
                {
                    "trx_id": "b697a5bef552dd46aeb18bc7cca4ca4f24c823eb",
                    "block": 41745896,
                    "trx_in_block": 8,
                    "op_in_trx": 0,
                    "virtual_op": False,
                    "timestamp": "2020-03-18T01:11:42",
                    "op": {
                        "type": "comment_operation",
                        "value": {
                            "parent_author": "hiveio",
                            "parent_permlink": "announcing-the-launch-of-hive-blockchain",
                            "author": "lecumberre",
                            "permlink": "q7d8qu",
                            "title": "",
                            "body": "This is  really  interesting.  I  will  be  present.   Success,  and  God  bless  you.",
                            "json_metadata": '{"app":"steemit/0.2"}',
                        },
                    },
                    "operation_id": 0,
                },
            ],
            [
                999,
                {
                    "trx_id": "7a31d99559a3d93526bd1a05fd9fa0f55b1ebcb8",
                    "block": 41745898,
                    "trx_in_block": 13,
                    "op_in_trx": 0,
                    "virtual_op": False,
                    "timestamp": "2020-03-18T01:11:48",
                    "op": {
                        "type": "vote_operation",
                        "value": {
                            "voter": "lecumberre",
                            "author": "hiveio",
                            "permlink": "announcing-the-launch-of-hive-blockchain",
                            "weight": 10000,
                        },
                    },
                    "operation_id": 0,
                },
            ],
        ]
    },
    "id": 1,
}
GET_OPS_IN_BLOCK = {
    "jsonrpc": "2.0",
    "result": {
        "ops": [
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 1,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "miners",
                        "creator": "miners",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 1,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:05:00",
                "op": {
                    "type": "producer_reward_operation",
                    "value": {
                        "producer": "initminer",
                        "vesting_shares": {"amount": "1000000", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 2,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "null",
                        "creator": "null",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 3,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "temp",
                        "creator": "temp",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 4,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "initminer",
                        "creator": "initminer",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
            {
                "trx_id": "0000000000000000000000000000000000000000",
                "block": 1,
                "trx_in_block": 4294967295,
                "op_in_trx": 5,
                "virtual_op": True,
                "timestamp": "2016-03-24T16:00:00",
                "op": {
                    "type": "account_created_operation",
                    "value": {
                        "new_account_name": "steem",
                        "creator": "steem",
                        "initial_vesting_shares": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                        "initial_delegation": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                    },
                },
                "operation_id": 0,
            },
        ]
    },
    "id": 1,
}
GET_TRANSACTION = {
    "jsonrpc": "2.0",
    "result": {
        "ref_block_num": 36374,
        "ref_block_prefix": 3218139339,
        "expiration": "2018-04-09T00:29:06",
        "operations": [
            {
                "type": "claim_reward_balance_operation",
                "value": {
                    "account": "social",
                    "reward_hive": {"amount": "0", "precision": 3, "nai": "@@000000021"},
                    "reward_hbd": {"amount": "0", "precision": 3, "nai": "@@000000013"},
                    "reward_vests": {"amount": "1", "precision": 6, "nai": "@@000000037"},
                },
            },
            {
                "type": "vote_operation",
                "value": {
                    "voter": "lecumberre",
                    "author": "hiveio",
                    "permlink": "announcing-the-launch-of-hive-blockchain",
                    "weight": 10000,
                },
            },
        ],
        "extensions": [],
        "signatures": [
            "1b01bdbb0c0d43db821c09ae8a82881c1ce3ba0eca35f23bc06541eca05560742f210a21243e20d04d5c88cb977abf2d75cc088db0fff2ca9fdf2cba753cf69844"
        ],
        "transaction_id": "6fde0190a97835ea6d9e651293e90c89911f933c",
        "block_num": 21401130,
        "transaction_num": 25,
    },
    "id": 1,
}
