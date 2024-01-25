from __future__ import annotations

import schemas.apis.condenser_api as ca
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.follow_api.fundaments_of_reponses import GetAccountReputationsDetail


class GetAccountReputations(PreconfiguredBaseModel):
    reputations: list[GetAccountReputationsDetail]


# aliases
GetFollowers = ca.GetFollowers
GetFollowing = ca.GetFollowing
GetFollowCount = ca.GetFollowCount
GetBlog = ca.GetBlog
GetBlogEntries = ca.GetBlogEntries
GetRebloggedBy = ca.GetRebloggedBy
