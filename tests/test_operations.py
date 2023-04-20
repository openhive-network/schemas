from __future__ import annotations

from typing import Any, Final

from pydantic import ValidationError

from schemas.__private.hive_fields_schemas import Authority
from schemas.operations import AccountCreateOperation, AccountUpdateOperation
from tests.hive_tests_constants import ACTIVE, MEMO_EXAMPLE_KEY, OWNER, POSTING

ACCOUNT_CREATE_OPERATION_VALID_DATA: Final[dict[str, Any]] = {
    "fee": "1.000 HIVE",
    "creator": "initminer",
    "new_account_name": "alice",
    "owner": OWNER,
    "active": ACTIVE,
    "posting": POSTING,
    "memo_key": MEMO_EXAMPLE_KEY,
    "json_metadata": "",
}


def test_account_create_operation() -> None:
    # ARRANGE
    test = AccountCreateOperation(**ACCOUNT_CREATE_OPERATION_VALID_DATA)
    invalid_data = ACCOUNT_CREATE_OPERATION_VALID_DATA.copy()

    # ACT
    invalid_data["creator"] = None
    invalid_data["memo_key"] = 1

    try:
        AccountCreateOperation(**invalid_data)
    except (ValueError, ValidationError) as e:
        error = str(e)
    # ASSERT
    assert test.creator == "initminer", test.fee == "1.000 HIVE"
    assert isinstance(test.owner, Authority)
    assert "none is not an allowed value" in error and "string does not match regex" in error


def test_account_update_operation() -> None:
    # ARRANGE
    AccountUpdateOperation(
        account="alice", owner=OWNER, active=ACTIVE, posting=POSTING, memo_key=MEMO_EXAMPLE_KEY, json_metadata=""
    )
    invalid_owner = OWNER.copy()

    # ACT
    invalid_owner["key_auths"][0].pop(0)

    try:
        AccountUpdateOperation(
            account=123,
            owner=invalid_owner,
            active=ACTIVE,
            posting=POSTING,
            memo_key=MEMO_EXAMPLE_KEY,
            json_metadata="",
        )
    except (ValueError, ValidationError) as e:
        str(e)
