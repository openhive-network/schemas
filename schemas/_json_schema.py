from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from msgspec import _json_schema as msgspec_json_schema
from msgspec import inspect as mi

if TYPE_CHECKING:
    from collections.abc import Iterable

__all__ = ("schema", "schema_components")


def schema(
    type_: Any,
    *,
    schema_hook: Callable[[type], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Generate a JSON Schema for a given type.

    Any schemas for (potentially) shared components are extracted and stored in
    a top-level ``"$defs"`` field.

    If you want to generate schemas for multiple types, or to have more control
    over the generated schema you may want to use ``schema_components`` instead.

    Parameters
    ----------
    type : type
        The type to generate the schema for.
    schema_hook : callable, optional
        An optional callback to use for generating JSON schemas of custom
        types. Will be called with the custom type, and should return a dict
        representation of the JSON schema for that type.

    Returns
    -------
    schema : dict
        The generated JSON Schema.

    See Also
    --------
    schema_components
    """
    (out,), components = schema_components((type_,), schema_hook=schema_hook)
    if components:
        out["$defs"] = components
    return out


def schema_components(
    types: Iterable[Any],
    *,
    schema_hook: Callable[[type], dict[str, Any]] | None = None,
    ref_template: str = "#/$defs/{name}",
) -> tuple[tuple[dict[str, Any], ...], dict[str, Any]]:
    """Generate JSON Schemas for one or more types.

    Any schemas for (potentially) shared components are extracted and returned
    in a separate ``components`` dict.

    Parameters
    ----------
    types : Iterable[type]
        An iterable of one or more types to generate schemas for.
    schema_hook : callable, optional
        An optional callback to use for generating JSON schemas of custom
        types. Will be called with the custom type, and should return a dict
        representation of the JSON schema for that type.
    ref_template : str, optional
        A template to use when generating ``"$ref"`` fields. This template is
        formatted with the type name as ``template.format(name=name)``. This
        can be useful if you intend to store the ``components`` mapping
        somewhere other than a top-level ``"$defs"`` field. For example, you
        might use ``ref_template="#/components/{name}"`` if generating an
        OpenAPI schema.

    Returns
    -------
    schemas : tuple[dict]
        A tuple of JSON Schemas, one for each type in ``types``.
    components : dict
        A mapping of name to schema for any shared components used by
        ``schemas``.

    See Also
    --------
    schema
    """
    type_infos = mi.multi_type_info(types)

    component_types = _collect_component_types(type_infos)

    name_map = msgspec_json_schema._build_name_map(component_types)

    gen = msgspec_json_schema._SchemaGenerator(name_map, schema_hook, ref_template)

    schemas = tuple(gen.to_schema(t) for t in type_infos)

    components = {name_map[cls]: gen.to_schema(t, False) for cls, t in component_types.items()}
    return schemas, components


def _collect_component_types(type_infos: Iterable[mi.Type]) -> dict[Any, mi.Type]:  # noqa: C901
    """Find all types in the type tree that are "nameable" and worthy of being
    extracted out into a shared top-level components mapping.

    Currently this looks for Struct, Dataclass, NamedTuple, TypedDict, and Enum
    types.
    """
    components = {}

    def collect(t):
        if isinstance(
            t, (mi.StructType, mi.TypedDictType, mi.DataclassType, mi.NamedTupleType)
        ):
            if t.cls not in components:
                components[t.cls] = t
                for f in t.fields:
                    collect(f.type)
        elif isinstance(t, mi.EnumType):
            components[t.cls] = t
        elif isinstance(t, mi.Metadata):
            collect(t.type)
        elif isinstance(t, mi.CollectionType):
            collect(t.item_type)
        elif isinstance(t, mi.TupleType):
            for st in t.item_types:
                collect(st)
        elif isinstance(t, mi.DictType):
            collect(t.key_type)
            collect(t.value_type)
        elif isinstance(t, mi.UnionType):
            for st in t.types:
                collect(st)

    for t in type_infos:
        collect(t)

    return components
