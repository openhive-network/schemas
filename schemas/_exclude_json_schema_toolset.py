from __future__ import annotations

import typing

import msgspec

FieldDictT = dict[str, msgspec.inspect.Field]
TreeExclusion = dict[str, "TreeExclusion | None"]

__all__ = ["TreeExclusion", "exclude_members", "merge_excluded_fields_for_schema_dictionaries"]


def _convert_type_to_annotation(tp: msgspec.inspect.Type) -> type[typing.Any]:  # noqa: C901, PLR0911, PLR0912
    if isinstance(tp, msgspec.inspect.CustomType | msgspec.inspect.NoneType):
        return type(None)
    if isinstance(tp, msgspec.inspect.StructType):
        return tp.cls
    if isinstance(tp, msgspec.inspect.UnionType):
        types_in_union: list[type[typing.Any]] = []
        for arg in tp.types:
            types_in_union.append(_convert_type_to_annotation(arg))
        return typing.Union[tuple(types_in_union)]  # type: ignore[return-value]
    if isinstance(tp, msgspec.inspect.ListType):
        item_type = _convert_type_to_annotation(tp.item_type)
        return typing.List[item_type]  # type: ignore[valid-type]
    if isinstance(tp, msgspec.inspect.DictType):
        key_type = _convert_type_to_annotation(tp.key_type)
        value_type = _convert_type_to_annotation(tp.value_type)
        return typing.Dict[key_type, value_type]  # type: ignore[valid-type]
    if isinstance(tp, msgspec.inspect.TupleType):
        item_types: list[type[typing.Any]] = []
        for item in tp.item_types:
            item_types.append(_convert_type_to_annotation(item))
        return typing.Tuple[tuple(item_types)]  # type: ignore[return-value]
    if isinstance(tp, msgspec.inspect.LiteralType):
        literal_values: list[typing.Any] = []
        for val in tp.values:
            literal_values.append(val)
        return typing.Literal[tuple(literal_values)]  # type: ignore[return-value]
    if isinstance(tp, msgspec.inspect.BoolType):
        return bool
    if isinstance(tp, msgspec.inspect.IntType):
        return int
    if isinstance(tp, msgspec.inspect.FloatType):
        return float
    if isinstance(tp, msgspec.inspect.StrType):
        return str
    if isinstance(tp, msgspec.inspect.BytesType):
        return bytes
    return typing.Any  # type: ignore[return-value]


def exclude_members_from_type(
    members_to_exclude: set[str], annotations: FieldDictT, cls_name: str, include: dict[str, type[typing.Any]]
) -> type[typing.Any]:
    from schemas._preconfigured_base_model import PreconfiguredBaseModel

    included_annotation: dict[str, msgspec.inspect.Type] = {}
    for field_name, field in annotations.items():
        if field.name not in members_to_exclude:
            included_annotation[field_name] = field.type

    included_annotation_flat = [(k, _convert_type_to_annotation(v)) for (k, v) in included_annotation.items()]
    included_annotation_flat.extend(list(include.items()))

    return msgspec.defstruct(
        name=cls_name, fields=included_annotation_flat, bases=(PreconfiguredBaseModel,), kw_only=True
    )

def ensure_struct_type(tp: msgspec.inspect.Type) -> msgspec.inspect.StructType:
    if isinstance(tp, msgspec.inspect.StructType):
        return tp
    if isinstance(tp, msgspec.inspect.UnionType):
        for arg in tp.types:
            if isinstance(arg, msgspec.inspect.StructType):
                return arg
    raise TypeError(f"Type {tp} is not a StructType nor a UnionType containing a StructType")


def recursive_type_replace(paths_to_process: TreeExclusion, annotations: FieldDictT, cls_name: str) -> type[typing.Any]:
    fields_to_exclude_by_me: set[str] = set()
    fields_excluded_by_others: dict[str, type[typing.Any]] = {}
    for field_name, sub_path in paths_to_process.items():
        fields_to_exclude_by_me.add(field_name)
        if isinstance(sub_path, dict):
            field_type = ensure_struct_type(annotations[field_name].type)
            fields_excluded_by_others[field_name] = recursive_type_replace(
                sub_path, convert_field_list_to_dict(field_type.fields), field_type.cls.__name__
            )

    return exclude_members_from_type(fields_to_exclude_by_me, annotations, cls_name, fields_excluded_by_others)


def convert_field_list_to_dict(field_list: tuple[msgspec.inspect.Field, ...]) -> FieldDictT:
    return {field.name: field for field in field_list}


def merge_excluded_fields_for_schema_dictionaries(
    from_super: TreeExclusion, from_child: TreeExclusion
) -> TreeExclusion:
    result: TreeExclusion = {}
    all_keys = set(from_super.keys()).union(set(from_child.keys()))
    for key in all_keys:
        if key in from_super and key not in from_child:
            result[key] = from_super[key]
            continue
        if key not in from_super and key in from_child:
            result[key] = from_child[key]
            continue

        super_value = from_super[key]
        child_value = from_child[key]
        if None in (super_value, child_value):
            result[key] = None
            continue
        assert isinstance(super_value, dict) and isinstance(child_value, dict), f"Invalid exclusion merge for key {key}"
        result[key] = merge_excluded_fields_for_schema_dictionaries(super_value, child_value)
    return result


T = typing.TypeVar("T")


def exclude_members(cls: type[T], exclusion_tree: TreeExclusion) -> type[T]:
    if len(exclusion_tree) == 0:
        return cls

    cls_type_info = typing.cast("msgspec.inspect.StructType", msgspec.inspect.type_info(cls))
    annotations_full = convert_field_list_to_dict(cls_type_info.fields)
    return recursive_type_replace(paths_to_process=exclusion_tree, annotations=annotations_full, cls_name=cls.__name__)
