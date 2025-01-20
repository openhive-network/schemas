from __future__ import annotations

import json
from schemas.apis import condenser_api
import schemas.fields.integers
from typing import Any, Final

import msgspec
import pytest

from schemas.apis.account_history_api.response_schemas import (
    GetTransaction,
)
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.jsonrpc import JSONRPCError, JSONRPCResult, get_response_model
import schemas.operations
from schemas.operations.claim_reward_balance_operation import ClaimRewardBalanceOperation
from schemas.operations.representation_types import LegacyRepresentationClaimRewardBalanceOperation
from tests.test_account_history_api import responses_from_api

from schemas.fields.resolvables import AssetUnion, JsonString, OptionallyEmpty
import schemas 


CUSTOM_JSON_OPERATION = {"required_auths": [], "required_posting_auths": [], "id": 3213, "json": "123"}

CUSTOM_JSON_OPERATION_TRANSACTION = {
    "jsonrpc": "2.0",
    "result": {"required_auths": ["bob"], "required_posting_auths": ["alice"], "id": "my_id", "json": {"dupa": "dupa"}},
    "id": 1,
}

def test_responses_from_api_correct_values() -> None:
    # ACT & ASSERT
    dupa = get_response_model(schemas.operations.CustomJsonOperation, json.dumps(CUSTOM_JSON_OPERATION_TRANSACTION), "hf26")

    # xd = dupa.result.json()
    pass