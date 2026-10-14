"""
Validation of JSON data (builtins) against msgspec models with Hive types from `schemas.fields`.

Hive types have a fixed JSON form (e.g. `AssetHive` - NAI form, `LegacyAssetHive` - legacy form), so no serialization
has to be given.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, TypeVar, Union, get_args, get_origin

import msgspec

from schemas.decoders import dec_hook_hf26

if TYPE_CHECKING:
    from collections.abc import Callable

__all__ = [
    "SchemaError",
    "is_matching_model",
    "validate",
    "validate_schema_field",
]

FieldT = TypeVar("FieldT")

_ROOT_PATH: Final[str] = "$"
_MSGSPEC_PATH: Final[re.Pattern[str]] = re.compile(r" - at `\$([^`]*)`$")


@dataclass(frozen=True, slots=True)
class SchemaError:
    path: str
    """Location of the problem in the data, e.g. `$[0].balance`."""
    message: str


def validate(data: object, model: object) -> list[SchemaError]:
    """
    Validate data against the given model.

    Args:
        data: Builtins, e.g. from `json.loads`.
        model: Type to validate against, e.g. `list[GetAccountsResponse]`.

    Returns:
        All found problems, empty list when the data matches the model.
    """
    try:
        _convert(data, model)
    except msgspec.ValidationError:
        errors: list[SchemaError] = []
        _collect_errors(data, model, _ROOT_PATH, errors)
        return errors
    return []


def validate_schema_field(data: object, field_type: Callable[[object], FieldT]) -> FieldT:
    """
    Create a value of the given field type (e.g. `AccountName`) from the data.

    Raises:
        schemas.errors.ValidationError: When the data does not match the field type.
    """
    return field_type(data)


def is_matching_model(data: object, field_type: Callable[[object], object]) -> bool:
    """Check if the data matches the given field type (e.g. `AccountName`)."""
    try:
        validate_schema_field(data, field_type)
    except msgspec.ValidationError:
        return False
    return True


def _convert(data: object, type_: object) -> object:
    return msgspec.convert(data, type=type_, dec_hook=dec_hook_hf26)


def _collect_errors(data: object, type_: object, path: str, errors: list[SchemaError]) -> None:
    try:
        _convert(data, type_)
    except msgspec.ValidationError as error:
        failure = error
    else:
        return

    errors_before = len(errors)
    _descend(data, type_, path, errors)
    if len(errors) == errors_before:  # nothing more precise found inside - report error of this node
        errors.append(SchemaError(_error_path(failure, path), _MSGSPEC_PATH.sub("", str(failure))))


def _descend(data: object, type_: object, path: str, errors: list[SchemaError]) -> None:
    if isinstance(type_, type) and issubclass(type_, msgspec.Struct) and isinstance(data, dict):
        _descend_struct(data, type_, path, errors)
        return

    origin = get_origin(type_)
    args = get_args(type_)
    if origin in (list, tuple, set, frozenset) and args and isinstance(data, list):
        if origin is tuple and not (len(args) == 2 and args[1] is Ellipsis):  # noqa: PLR2004
            return
        for index, item in enumerate(data):
            _collect_errors(item, args[0], f"{path}[{index}]", errors)
        return

    if origin is dict and len(args) == 2 and isinstance(data, dict):  # noqa: PLR2004
        for key, item in data.items():
            _collect_errors(item, args[1], f"{path}.{key}", errors)
        return

    if origin is Union or type(type_).__name__ == "UnionType":
        structs = [arg for arg in args if isinstance(arg, type) and issubclass(arg, msgspec.Struct)]
        if isinstance(data, dict) and len(structs) == 1:
            _descend_struct(data, structs[0], path, errors)


def _descend_struct(data: dict[str, object], type_: type[msgspec.Struct], path: str, errors: list[SchemaError]) -> None:
    fields = msgspec.structs.fields(type_)
    known_names = {field.encode_name for field in fields}
    for field in fields:
        if field.encode_name in data:
            _collect_errors(data[field.encode_name], field.type, f"{path}.{field.encode_name}", errors)
        elif field.required:
            errors.append(SchemaError(path, f"Object missing required field `{field.encode_name}`"))

    if getattr(type_, "__struct_config__", None) is not None and type_.__struct_config__.forbid_unknown_fields:
        errors.extend(
            SchemaError(f"{path}.{key}", f"Object contains unknown field `{key}`")
            for key in data
            if key not in known_names
        )


def _error_path(error: Exception, path: str) -> str:
    match = _MSGSPEC_PATH.search(str(error))
    return f"{path}{match.group(1)}" if match else path
