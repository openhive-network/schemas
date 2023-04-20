from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas_strict import Int16t
from schemas.__private.operations_strict.vote_operation_strict import VoteOperationStrict

DEFAULT_WEIGHT: Final[Int16t] = Int16t(0)


class VoteOperation(VoteOperationStrict):
    weight: Int16t = DEFAULT_WEIGHT
