from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from collections.abc import Callable

    from pydantic.typing import AbstractSetIntStr, CallableGenerator, MappingIntStrAny


class ApplicationOperation(PreconfiguredBaseModel):
    __operation_name__: str

    @classmethod
    def get_name(cls) -> str:
        return cls.__operation_name__

    @classmethod
    # TODO[pydantic]: We couldn't refactor `__get_validators__`, please create the `__get_pydantic_core_schema__` manually.
    # Check https://docs.pydantic.dev/latest/migration/#defining-custom-types for more information.
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> Self:
        if isinstance(value, cls):
            return value

        if isinstance(value, str):
            try:
                parsed = json.loads(str(value))
                return cls(**parsed)
            except (ValueError, TypeError) as error:
                raise ValueError(f"Value is not a valid application operation string! Received `{value}`") from error

        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

    def json(  # noqa: PLR0913
        self,
        *,
        include: AbstractSetIntStr | MappingIntStrAny | None = None,
        exclude: AbstractSetIntStr | MappingIntStrAny | None = None,
        by_alias: bool = True,  # modified, most of the time we want to dump by alias
        skip_defaults: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        encoder: Callable[[Any], Any] | None = None,
        models_as_dict: bool = True,
        ensure_ascii: bool = False,  # modified, so unicode characters are not escaped, will properly dump e.g. polish characters
        **dumps_kwargs: Any,
    ) -> str:
        return super().json(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            encoder=encoder,
            models_as_dict=models_as_dict,
            ensure_ascii=ensure_ascii,
            separators=(",", ":"),
            **dumps_kwargs,
        )
