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
    """This is an extension of a function from the msgspec module, implemented here to add support for excluding fields."""
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
    """This is an extension of a function from the msgspec module, implemented here to add support for excluding fields."""

    type_infos = mi.multi_type_info(types)

    component_types = _collect_component_types(type_infos)

    name_map = msgspec_json_schema._build_name_map(component_types)

    gen = msgspec_json_schema._SchemaGenerator(name_map, schema_hook, ref_template)

    schemas = tuple(gen.to_schema(t) for t in type_infos)

    components = {name_map[cls]: gen.to_schema(t, False) for cls, t in component_types.items()}
    return schemas, components


def _collect_component_types(type_infos: Iterable[mi.Type]) -> dict[Any, mi.Type]:  # noqa: C901
    """This is an extension of a function from the msgspec module, implemented here to add support for excluding fields."""

    components: dict[Any, mi.Type] = {}

    def _exclude(t: mi.Type) -> mi.Type:
        if isinstance(t, mi.StructType) and hasattr(t.cls, "excluded_fields_for_schema_json"):
            excluded: set[str] = t.cls.excluded_fields_for_schema_json()
            if excluded:
                t.fields = tuple(x for x in t.fields if x.name not in excluded)
        return t

    def collect(t: mi.Type) -> None:  # noqa: C901
        t = _exclude(t)
        if isinstance(t, (mi.StructType, mi.TypedDictType, mi.DataclassType, mi.NamedTupleType)):
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
