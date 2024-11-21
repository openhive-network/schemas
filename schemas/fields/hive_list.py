from __future__ import annotations

from typing import List, TYPE_CHECKING, Generic

from pydantic import Field, ConstrainedList

from schemas._preconfigured_base_model import BaseModelT
from typing_extensions import Annotated

__all__ = ["HiveList", "EmptyList"]

if TYPE_CHECKING:
    HiveList = list

    class EmptyList(ConstrainedList):
        max_items = 0
        item_type = str

else:

    class HiveList(ConstrainedList, Generic[BaseModelT]):
        """Some responses could return empty list, it should not raise any error. This type makes it possible"""

        min_items = 0

    EmptyList = Annotated[List[str], Field(max_items=0)]
