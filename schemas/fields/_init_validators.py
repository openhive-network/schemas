from __future__ import annotations

from collections.abc import Callable
from threading import Lock
from typing import Annotated, Any, Generic, TypeVar, cast

import msgspec
from typing_extensions import Self

from schemas.fields.serializable import Serializable

__all__ = [
    "InitValidator",
    "ValidatorString",
    "ValidatorInt",
]

T = TypeVar("T")
ValidatorParamT_contra = TypeVar("ValidatorParamT_contra", contravariant=True)
ValidatorResultT_co = TypeVar("ValidatorResultT_co", covariant=True)

RegisteredTypesValue = type["InitValidator[Any]"]
RegisteredTypes = dict[str, RegisteredTypesValue]


ValidatorCallback = Callable[[ValidatorParamT_contra], ValidatorResultT_co]

_registered_types: RegisteredTypes = {}
_registered_types_lock = Lock()


def register_new_type(name: str, new_type: RegisteredTypesValue) -> None:
    with _registered_types_lock:
        _registered_types[name] = new_type


def find_registered_type(name: str) -> RegisteredTypesValue | None:
    with _registered_types_lock:
        return _registered_types.get(name)


def get_copy_of_registered_types() -> RegisteredTypes:
    with _registered_types_lock:
        return _registered_types.copy()


class InitValidator(Serializable, Generic[T]):
    """Base class for types that performs validation during initialization and decode using msgspec library."""

    def __new__(cls, obj: Any, *, skip_validation: bool = False) -> Self:  # noqa: ARG003
        return super().__new__(cls)

    @classmethod
    def validate(cls, value: T) -> Self:
        return cls(
            msgspec.convert(value, type=Annotated[cls._covered_type(), cls._meta()], strict=False),
            skip_validation=True,
        )

    _not_implemented_msg = "Make sure to use types created using InitValidator.factory() classmethod"

    @classmethod
    def _meta(cls) -> msgspec.Meta:
        raise NotImplementedError(cls._not_implemented_msg)

    @classmethod
    def _covered_type(cls) -> type[T]:
        raise NotImplementedError(cls._not_implemented_msg)

    @classmethod
    def factory(
        cls,
        name: str,
        meta: msgspec.Meta,
        *,
        pre_validator: ValidatorCallback[T, T] = lambda x: x,
        post_validator: ValidatorCallback[Any, Any] = lambda x: x,
        skip_default_validation: bool = False,
    ) -> type[T]:
        if (registered_type := find_registered_type(name)) is not None:
            return cast(type[T], registered_type)

        class InitMetaValidator(cls):  # type: ignore[valid-type, misc]
            @classmethod
            def _meta(cls) -> msgspec.Meta:
                return meta

            @classmethod
            def validate(cls, value: T) -> Self:
                validated = pre_validator(value)
                if not skip_default_validation:
                    validated = super().validate(validated)
                return cast(Self, post_validator(validated))

        new_type = type(name, (InitMetaValidator,), {})
        register_new_type(name, new_type)
        return new_type

    @staticmethod
    def get_registered_types() -> RegisteredTypes:
        return get_copy_of_registered_types()

    def serialize(self) -> Any:
        return self._covered_type()(self)  # type: ignore[call-arg]


class ValidatorString(str, InitValidator[str]):
    def __new__(cls, obj: Any, *, skip_validation: bool = False) -> Self:
        if not skip_validation:
            cls.validate(cls._covered_type()(obj))
        return super().__new__(cls, obj)

    @classmethod
    def _covered_type(cls) -> type[str]:
        return str


class ValidatorInt(int, InitValidator[int]):
    def __new__(cls, obj: Any, *, skip_validation: bool = False) -> Self:
        if not skip_validation:
            cls.validate(cls._covered_type()(obj))
        return super().__new__(cls, obj)

    @classmethod
    def _covered_type(cls) -> type[int]:
        return int
