from __future__ import annotations

from typing import TYPE_CHECKING



__all__ = [
    "HiveList",
]


if TYPE_CHECKING:
    HiveList = list

else:

    # class HiveList(ConstrainedList, Generic[BaseModelT]):
    #     """Some responses could return empty list, it should not raise any error. This type makes it possible"""

    #     min_items = 0
    
    # HiveList = Annotated[list[Any], msgspec.Meta(min_length=0)]

    HiveList = list