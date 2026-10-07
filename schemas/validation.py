"""
Explicit, opt-in validation of API responses.

API calls never validate responses. An application which wants to check a response calls `validate_schema`,
either with the validation model generated for the endpoint or with its own model (e.g. describing only the
subset of fields it uses).

Generated API packages register where their validation models live:

- per API name, with `register_validation_models` (used when the endpoint is given as `"api_name.method"`),
- per client class, with `__validation_module__` / `__serialization__` class attributes (used when the endpoint
  is given as a method, e.g. `chain.api.condenser_api.get_accounts`; this works for any API collection joined
  with `extends`).

A validation module exposes `ENDPOINT_RESULTS: dict[str, tuple[type | str, bool]]` (method name -> result model or
name of the module attribute holding it, whether the result is an array).
"""

from __future__ import annotations

import dataclasses
import importlib
import json
import re
from dataclasses import dataclass
from threading import Lock
from typing import TYPE_CHECKING, Any, Final, Literal, Union, get_args, get_origin

if TYPE_CHECKING:
    from collections.abc import Callable, Mapping
    from types import ModuleType

__all__ = [
    "JsonT",
    "SchemaError",
    "SerializationT",
    "UnknownEndpointError",
    "convert_to_validation_schema",
    "register_validation_models",
    "validate_schema",
]

JsonT = dict[str, Any] | list[Any] | str | int | float | bool | None
SerializationT = Literal["hf26", "legacy"]

_ROOT_PATH: Final[str] = "$"
_MSGSPEC_PATH_SUFFIX: Final[re.Pattern[str]] = re.compile(r" - at `\$[^`]*`$")


@dataclass(frozen=True, slots=True)
class SchemaError:
    path: str
    """Location of the problem in the response, e.g. `$[0].balance`."""
    message: str


class UnknownEndpointError(ValueError):
    """Raised when there is no validation model for the given endpoint."""


@dataclass(frozen=True, slots=True)
class _Registration:
    module: str
    serialization: SerializationT


_registry: dict[str, _Registration] = {}
_registry_lock = Lock()


def register_validation_models(api_name: str, module_path: str, serialization: SerializationT = "hf26") -> None:
    """
    Register the module with validation models of the given API.

    Args:
        api_name: Name of the API, e.g. `condenser_api`.
        module_path: Dotted path of the validation module (imported lazily, on first validation).
        serialization: Serialization used by the API responses (`legacy` e.g. for condenser_api).
    """
    with _registry_lock:
        _registry[api_name] = _Registration(module_path, serialization)


def convert_to_validation_schema(
    response: Any,
    endpoint: str | Callable[..., Any],
    *,
    model: Any | None = None,
    serialization: SerializationT | None = None,
) -> Any:
    """
    Convert a response of the given endpoint to its validation model (Hive types from `schemas.fields`).

    Args:
        response: Response to convert - builtins (e.g. from `json.loads`), raw JSON as `bytes`, or result returned by
                  an API call (public models are converted back to builtins, including undeclared fields).
        endpoint: `"api_name.method"` or the API method itself (e.g. `chain.api.condenser_api.get_accounts`).
        model: Type to convert to instead of the generated validation model (e.g. `list[MyAccount]`).
        serialization: Override of the serialization (`hf26`/`legacy`) used to decode Hive types.

    Returns:
        Instance of the validation model (assets as asset objects, timestamps as datetimes, ...).

    Raises:
        UnknownEndpointError: When `model` is not given and there is no validation model for the endpoint.
        schemas.errors.ValidationError: When the response does not match the model - use `validate_schema` to get
            all problems with their paths.
    """
    target, dec_hook = _target_and_hook(endpoint, model, serialization)
    return _convert(_to_builtins(response), target, dec_hook)


def validate_schema(
    response: Any,
    endpoint: str | Callable[..., Any],
    *,
    model: Any | None = None,
    serialization: SerializationT | None = None,
) -> list[SchemaError]:
    """
    Validate a response of the given endpoint.

    Same arguments as `convert_to_validation_schema`; instead of the converted model returns the found problems.

    Returns:
        All found problems, empty list when the response matches the model.

    Raises:
        UnknownEndpointError: When `model` is not given and there is no validation model for the endpoint.
    """
    target, dec_hook = _target_and_hook(endpoint, model, serialization)
    data = _to_builtins(response)
    try:
        _convert(data, target, dec_hook)
    except _conversion_errors():
        errors: list[SchemaError] = []
        _collect_errors(data, target, _ROOT_PATH, dec_hook, errors)
        return errors
    return []


def _target_and_hook(
    endpoint: str | Callable[..., Any], model: Any | None, serialization: SerializationT | None
) -> tuple[Any, Callable[[type, Any], Any]]:
    registration, method = _resolve_endpoint(endpoint)
    target = model if model is not None else _generated_model(registration, method)
    return target, _dec_hook(serialization or registration.serialization)


def _convert(data: Any, target: Any, dec_hook: Callable[[type, Any], Any]) -> Any:
    import msgspec

    return msgspec.convert(data, type=target, dec_hook=dec_hook)


def _conversion_errors() -> tuple[type[Exception], ...]:
    """Errors meaning that data does not match the model (custom field validators may raise the builtin ones)."""
    import msgspec

    return (msgspec.ValidationError, ValueError, TypeError, AssertionError)


def _resolve_endpoint(endpoint: str | Callable[..., Any]) -> tuple[_Registration, str]:
    if isinstance(endpoint, str):
        api_name, _, method = endpoint.rpartition(".")
        with _registry_lock:
            registration = _registry.get(api_name)
        if registration is None:
            raise UnknownEndpointError(f"No validation models registered for API `{api_name}` (endpoint `{endpoint}`).")
        return registration, method

    owner = _owner_class(endpoint)
    module = getattr(owner, "__validation_module__", None)
    if not isinstance(module, str):
        raise UnknownEndpointError(f"API class `{owner.__qualname__}` does not define `__validation_module__`.")
    serialization: SerializationT = getattr(owner, "__serialization__", "hf26")
    return _Registration(module, serialization), endpoint.__name__


def _owner_class(endpoint: Callable[..., Any]) -> type[Any]:
    bound_to = getattr(endpoint, "__self__", None)
    if bound_to is not None:
        return bound_to if isinstance(bound_to, type) else type(bound_to)

    module = importlib.import_module(endpoint.__module__)
    owner: Any = module
    for part in endpoint.__qualname__.split(".")[:-1]:
        owner = getattr(owner, part)
    if not isinstance(owner, type):
        raise UnknownEndpointError(f"Cannot find API class of `{endpoint.__qualname__}`.")
    return owner


def _generated_model(registration: _Registration, method: str) -> Any:
    module: ModuleType = importlib.import_module(registration.module)
    results: Mapping[str, tuple[Any, bool]] = module.ENDPOINT_RESULTS
    if method not in results:
        raise UnknownEndpointError(f"No validation model for method `{method}` in `{registration.module}`.")
    result_model, is_array = results[method]
    if isinstance(result_model, str):
        result_model = getattr(module, result_model)
    return list[result_model] if is_array else result_model  # type: ignore[valid-type]


def _dec_hook(serialization: SerializationT) -> Callable[[type, Any], Any]:
    from schemas.decoders import dec_hook_hf26, dec_hook_legacy

    return dec_hook_legacy if serialization == "legacy" else dec_hook_hf26


def _to_builtins(response: Any, *, top_level: bool = True) -> Any:
    if top_level and isinstance(response, bytes | bytearray):
        return json.loads(response)
    if dataclasses.is_dataclass(response) and not isinstance(response, type):
        serialize = getattr(response, "json", None)
        if callable(serialize):
            return json.loads(serialize())
    if isinstance(response, list | tuple):
        return [_to_builtins(item, top_level=False) for item in response]
    return response


def _collect_errors(
    data: Any, type_: Any, path: str, dec_hook: Callable[[type, Any], Any], errors: list[SchemaError]
) -> None:
    try:
        _convert(data, type_, dec_hook)
    except _conversion_errors() as error:
        failure = error
    else:
        return

    errors_before = len(errors)
    _descend(data, type_, path, dec_hook, errors)
    if len(errors) == errors_before:  # nothing more precise found inside - report error of this node
        errors.append(SchemaError(_error_path(failure, path), _MSGSPEC_PATH_SUFFIX.sub("", str(failure))))


def _descend(data: Any, type_: Any, path: str, dec_hook: Callable[[type, Any], Any], errors: list[SchemaError]) -> None:
    import msgspec

    if isinstance(type_, type) and issubclass(type_, msgspec.Struct) and isinstance(data, dict):
        _descend_struct(data, type_, path, dec_hook, errors)
        return

    origin = get_origin(type_)
    args = get_args(type_)
    if origin in (list, tuple, set, frozenset) and args and isinstance(data, list):
        if origin is tuple and not (len(args) == 2 and args[1] is Ellipsis):  # noqa: PLR2004
            return
        for index, item in enumerate(data):
            _collect_errors(item, args[0], f"{path}[{index}]", dec_hook, errors)
        return

    if origin is dict and len(args) == 2 and isinstance(data, dict):  # noqa: PLR2004
        for key, item in data.items():
            _collect_errors(item, args[1], f"{path}.{key}", dec_hook, errors)
        return

    if origin is Union or type(type_).__name__ == "UnionType":
        structs = [arg for arg in args if isinstance(arg, type) and issubclass(arg, msgspec.Struct)]
        if isinstance(data, dict) and len(structs) == 1:
            _descend_struct(data, structs[0], path, dec_hook, errors)


def _descend_struct(
    data: dict[str, Any], type_: Any, path: str, dec_hook: Callable[[type, Any], Any], errors: list[SchemaError]
) -> None:
    import msgspec

    fields = msgspec.structs.fields(type_)
    known_names = {field.encode_name for field in fields}
    for field in fields:
        if field.encode_name in data:
            _collect_errors(data[field.encode_name], field.type, f"{path}.{field.encode_name}", dec_hook, errors)
        elif field.required:
            errors.append(SchemaError(path, f"Object missing required field `{field.encode_name}`"))

    if getattr(type_, "__struct_config__", None) is not None and type_.__struct_config__.forbid_unknown_fields:
        errors.extend(
            SchemaError(f"{path}.{key}", f"Object contains unknown field `{key}`")
            for key in data
            if key not in known_names
        )


def _error_path(error: Exception, path: str) -> str:
    match = re.search(r" - at `\$([^`]*)`$", str(error))
    return f"{path}{match.group(1)}" if match else path
