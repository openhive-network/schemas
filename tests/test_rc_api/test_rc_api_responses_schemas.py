from __future__ import annotations

from typing import Any

import pytest

from schemas.apis.rc_api import (
    FindRcAccounts,
    GetResourceParams,
    GetResourcePool,
    ListRcAccounts,
    ListRcDirectDelegations,
)
from schemas.jsonrpc import get_response_model

from .reponses_from_api import (
    FIND_RC_ACCOUNTS,
    GET_RESOURCE_PARAMS,
    GET_RESOURCE_POOL,
    LIST_RC_ACCOUNTS,
    LIST_RC_DIRECT_DELEGATIONS,
)


@pytest.mark.parametrize(
    "parameters, schema, endpoint",
    [
        (FIND_RC_ACCOUNTS, FindRcAccounts, "rc_api.find_rc_accounts"),
        (GET_RESOURCE_PARAMS, GetResourceParams, "rc_api.get_resource_params"),
        (GET_RESOURCE_POOL, GetResourcePool, "rc_api.get_resource_pool"),
        (LIST_RC_ACCOUNTS, ListRcAccounts, "rc_api.list_rc_accounts"),
        (LIST_RC_DIRECT_DELEGATIONS, ListRcDirectDelegations, "rc_api.list_rc_direct_delegations"),
    ],
)
def test_schemas_of_database_api_responses(parameters: dict[str, Any], schema: Any, endpoint: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, endpoint, **parameters)
