from __future__ import annotations

from typing import TYPE_CHECKING, Generic

from pydantic import ConstrainedList

from schemas._preconfigured_base_model import BaseModelT

__all__ = [
    "HiveList",
]


if TYPE_CHECKING:
    HiveList = list

else:

    class HiveList(ConstrainedList, Generic[BaseModelT]):
        """Some responses could return empty list, it should not raise any error. This type makes it possible"""

        min_items = 0
