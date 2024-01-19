from __future__ import annotations

import json
from typing import TYPE_CHECKING

from pydantic import ConstrainedStr

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class JsonString(ConstrainedStr):
    """From this data type it must be possible to create json from, but it still must stay an string"""

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate
        yield from super().__get_validators__()

    @classmethod
    def validate(cls, value: str) -> str:
        error_template = ValueError("The value could only string that can be converted to json!")

        if not isinstance(value, str):
            raise error_template

        try:
            json.loads(value)
        except (ValueError, TypeError) as error:
            raise error_template from error

        return value
