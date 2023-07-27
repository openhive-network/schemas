from __future__ import annotations

from typing import Any

import pytest

from schemas.hive_factory import HiveResult
from schemas.rc_api import FindRcAccounts, GetResourceParams, GetResourcePool, ListRcAccounts, ListRcDirectDelegations

from .reponses_from_api import (
    FIND_RC_ACCOUNTS,
    GET_RESOURCE_PARAMS,
    GET_RESOURCE_POOL,
    LIST_RC_ACCOUNTS,
    LIST_RC_DIRECT_DELEGATIONS,
)


@pytest.mark.parametrize(
    "parameters, schema",
    [
        (FIND_RC_ACCOUNTS, FindRcAccounts),
        (GET_RESOURCE_PARAMS, GetResourceParams),
        (GET_RESOURCE_POOL, GetResourcePool),
        (LIST_RC_ACCOUNTS, ListRcAccounts),
        (LIST_RC_DIRECT_DELEGATIONS, ListRcDirectDelegations),
    ],
)
def test_schemas_of_database_api_responses(parameters: dict[str, Any], schema: Any) -> None:
    # ACT & ASSERT
    HiveResult.factory(schema, **parameters)
