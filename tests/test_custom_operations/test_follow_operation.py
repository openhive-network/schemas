from __future__ import annotations

from typing import Final

from schemas.custom_operations.follow_operation import FollowOperation, FollowOperationLegacyRepresentation
from schemas.operations.custom_json_operation import CustomJsonOperation

from .helpers import assert_json_contains

CUSTOM_JSON_ID: Final[str] = "my_id"
FOLLOW_OPERATION_JSON_STRING: Final[str] = '["follow",{"follower":"abs","following":"xyz","what":["blog"]}]'


def test_dump_follow_operation() -> None:
    # ARRANGE
    follow_operation = FollowOperation(follower="abs", following="xyz", what=["blog"])
    follow_operation_legacy = FollowOperationLegacyRepresentation(value=follow_operation)

    # ACT
    op = CustomJsonOperation[FollowOperationLegacyRepresentation](
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=follow_operation_legacy
    )

    # ASSERT
    assert_json_contains(follow_operation_legacy.json(), op.json())


def test_load_follow_operation() -> None:
    # ACT
    op = CustomJsonOperation[FollowOperationLegacyRepresentation](
        required_auths=[], required_posting_auths=[], id_=CUSTOM_JSON_ID, json_=FOLLOW_OPERATION_JSON_STRING
    )

    # ASSERT
    assert_json_contains(FOLLOW_OPERATION_JSON_STRING, op.json())
