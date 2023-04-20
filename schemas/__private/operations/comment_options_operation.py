from __future__ import annotations

from typing import Final

from schemas.__private.hive_constants import HIVE_100_PERCENT
from schemas.__private.hive_fields_schemas_strict import Uint16t
from schemas.__private.operations_strict.comment_options_operation_strict import CommentOptionsOperationStrict

DEFAULT_ALLOW_VOTES: Final[bool] = True
DEFAULT_ALLOW_CURATION_REWARDS: Final[bool] = True


class CommentOptionsOperation(CommentOptionsOperationStrict):
    percent_hbd: Uint16t = Uint16t(HIVE_100_PERCENT)
    allow_votes: bool = DEFAULT_ALLOW_VOTES
    allow_curation_rewards: bool = DEFAULT_ALLOW_CURATION_REWARDS
