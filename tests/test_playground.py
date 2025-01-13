from __future__ import annotations

import json
from typing import Any

import msgspec
import pytest

from schemas.apis.account_history_api.response_schemas import (
    GetTransaction,
)
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.jsonrpc import JSONRPCError, JSONRPCResult, get_response_model
from schemas.operations.claim_reward_balance_operation import ClaimRewardBalanceOperation
from schemas.operations.representation_types import LegacyRepresentationClaimRewardBalanceOperation

def enc_hook(value):
    if isinstance(value, (AssetHbd | AssetHive | AssetVest)):
        return value.as_legacy()

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

GET_TRANSACTION_LEGACY = {
    "jsonrpc": "2.0",
    "result": {
        "ref_block_num": 36374,
        "ref_block_prefix": 3218139339,
        "expiration": "2018-04-09T00:29:06",
        "operations": [
            [
                "claim_reward_balance",
                {
                    "account": "social",
                    "reward_hive": "0.000 HIVE",
                    "reward_hbd": "0.000 HBD",
                    "reward_vests": "1.000000 VESTS",
                },
            ],
            # {
            #     "type": "vote_operation",
            #     "value": {
            #         "voter": "lecumberre",
            #         "author": "hiveio",
            #         "permlink": "announcing-the-launch-of-hive-blockchain",
            #         "weight": 10000,
            #     },
            # },
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
x = LegacyRepresentationClaimRewardBalanceOperation(value=ClaimRewardBalanceOperation(account="bob", reward_hive=AssetHive(amount=0), reward_hbd=AssetHbd(amount=0), reward_vests=AssetVest(amount=1)))
encoder = msgspec.json.Encoder(enc_hook=enc_hook)


def test_account_history_api_correct_values() -> None:
    dupa = encoder.encode(x)
    # ARRANGE
    pattern = json.dumps(GET_TRANSACTION, sort_keys=True)

    # ACT
    parsed = get_response_model(GetTransaction, json.dumps(GET_TRANSACTION))
    reserialized = parsed.json(by_alias=True, sort_keys=True)

    # ASSERT
    assert pattern == reserialized
