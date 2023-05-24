from __future__ import annotations

from typing import Any

import pytest

from schemas.__private.hive_factory import HiveResult
from schemas.condenser_api.response_schemas import (
    GetDiscussionsByAuthorBeforeDate,
    GetDiscussionsByBlog,
    GetDiscussionsByComments,
    GetDiscussionsByCreated,
    GetDiscussionsByFeed,
    GetDiscussionsByHot,
    GetDiscussionsByTrending,
    GetDynamicGlobalProperties,
    GetFeedHistory,
    GetPostDiscussionsByPayout,
    GetRepliesByLastUpdate,
)
from tests.test_condenser_api.responses_from_api import (
    GET_DISCUSSIONS_BY_AUTHOR_BEFORE_DATE,
    GET_DISCUSSIONS_BY_BLOG,
    GET_DISCUSSIONS_BY_COMMENTS,
    GET_DISCUSSIONS_BY_CREATED,
    GET_DISCUSSIONS_BY_FEED,
    GET_DISCUSSIONS_BY_HOT,
    GET_DISCUSSIONS_BY_TRENDING,
    GET_DYNAMIC_GLOBAL_PROPERTIES,
    GET_FEED_HISTORY,
    GET_POST_DISCUSSION_BY_PAYOUT,
    GET_REPLIES_BY_LAST_UPDATE,
)


@pytest.mark.parametrize(
    "schema, parameters",
    [
        (GetDiscussionsByAuthorBeforeDate, GET_DISCUSSIONS_BY_AUTHOR_BEFORE_DATE),
        (GetDiscussionsByBlog, GET_DISCUSSIONS_BY_BLOG),
        (GetDiscussionsByComments, GET_DISCUSSIONS_BY_COMMENTS),
        (GetDiscussionsByCreated, GET_DISCUSSIONS_BY_CREATED),
        (GetDiscussionsByFeed, GET_DISCUSSIONS_BY_FEED),
        (GetDiscussionsByHot, GET_DISCUSSIONS_BY_HOT),
        (GetDiscussionsByTrending, GET_DISCUSSIONS_BY_TRENDING),
        (GetDynamicGlobalProperties, GET_DYNAMIC_GLOBAL_PROPERTIES),
        (GetFeedHistory, GET_FEED_HISTORY),
        (GetPostDiscussionsByPayout, GET_POST_DISCUSSION_BY_PAYOUT),
        (GetRepliesByLastUpdate, GET_REPLIES_BY_LAST_UPDATE),
    ],
)
def test_condenser_api_correct_values(schema: Any, parameters: Any) -> None:
    # ACT & ASSERT
    HiveResult.factory(schema, **parameters)
