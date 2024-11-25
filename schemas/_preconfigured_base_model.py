"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

import types
import typing
from datetime import datetime
from typing import Any, TypeVar, get_args, get_origin

import pydantic
from pydantic import ConfigDict, BaseModel, Field, create_model  # pyright: ignore
from typing_extensions import Self

from schemas.fields.serializable import Serializable
from schemas.hive_constants import HIVE_TIME_FORMAT

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from pydantic.typing import AbstractSetIntStr, DictStrAny, MappingIntStrAny


class PreconfiguredBaseModel(BaseModel):
    # TODO[pydantic]: The following keys were removed: `smart_union`, `json_encoders`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


BaseModelT = TypeVar("BaseModelT", bound=PreconfiguredBaseModel)
