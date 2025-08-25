from __future__ import annotations

import typing
from typing import Any, Self, get_args, get_origin

import msgspec
from msgspec import json

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.decoders import dec_hook_hf26, schema_hook


T = typing.TypeVar("T", bound=PreconfiguredBaseModel)


def _is_marked_with_exclude_json_schema(annotation: msgspec.inspect.Type) -> bool:
    if not isinstance(annotation, msgspec.inspect.UnionType):
        return False

    for arg in annotation.types:
        if isinstance(arg, msgspec.inspect.StructType) and arg.cls.__name__ == "ExcludeFromJsonSchema":
            return True
    return False

def _exclude_marker_from_type(annotation: msgspec.inspect.Type) -> msgspec.inspect.Type | msgspec.inspect.UnionType:
    if not isinstance(annotation, msgspec.inspect.UnionType):
        return annotation
    new_types: list[msgspec.inspect.Type] = []

    for arg in annotation.types:
        if isinstance(arg, msgspec.inspect.StructType) and arg.cls.__name__ == "ExcludeFromJsonSchema":
            continue
        new_types.append(arg)

    return new_types[0] if len(new_types) == 1 else msgspec.inspect.UnionType(tuple(new_types))

def _convert_type_to_annotation(tp: msgspec.inspect.Type) -> type:
    if isinstance(tp, msgspec.inspect.StructType):
        return tp.cls
    if isinstance(tp, msgspec.inspect.UnionType):
        types_in_union = []
        for arg in tp.types:
            types_in_union.append(_convert_type_to_annotation(arg))
        return typing.Union[tuple(types_in_union)]
    if isinstance(tp, msgspec.inspect.ListType):
        item_type = _convert_type_to_annotation(tp.item_type)
        return typing.List[item_type]
    if isinstance(tp, msgspec.inspect.DictType):
        key_type = _convert_type_to_annotation(tp.key_type)
        value_type = _convert_type_to_annotation(tp.value_type)
        return typing.Dict[key_type, value_type]
    if isinstance(tp, msgspec.inspect.NoneType):
        return type(None)
    if isinstance(tp, msgspec.inspect.TupleType):
        item_types = []
        for item in tp.item_types:
            item_types.append(_convert_type_to_annotation(item))
        return typing.Tuple[tuple(item_types)]
    if isinstance(tp, msgspec.inspect.LiteralType):
        literal_values = []
        for val in tp.values:
            literal_values.append(val)
        return typing.Literal[tuple(literal_values)]
    if isinstance(tp, msgspec.inspect.AnyType):
        return typing.Any
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
    return tp

def excludes_json_schema(cls: type[T]) -> type[T]:
    """
    Class decorator that replaces all fields annotated as `T | ExcludeFromJsonSchema`
    with just `T` in the class __annotations__.
    """


    annotations: msgspec.inspect.StructType = msgspec.inspect.type_info(cls)
    excluded_annotation: dict[str, msgspec.inspect.Type] = {}
    new_annotations: dict[str, msgspec.inspect.Type] = {}
    for field in annotations.fields:
        if _is_marked_with_exclude_json_schema(field.type):
            new_type = _exclude_marker_from_type(field.type)
            new_annotations[field.name] = new_type
        else:
            excluded_annotation[field.name] = field.type
            new_annotations[field.name] = field.type

    excluded_annotation_flat = [(k, _convert_type_to_annotation(v)) for (k, v) in excluded_annotation.items()]
    new_annotations_flat = [(k, _convert_type_to_annotation(v)) for (k, v) in new_annotations.items()]

    prepared_cls = msgspec.defstruct(name=cls.__name__, fields=excluded_annotation_flat, bases=(PreconfiguredBaseModel,), kw_only=True)
    class OutputModel(cls):
        @classmethod
        def _cls_for_schema_json(cls) -> type[Self]:
            return prepared_cls
    return msgspec.defstruct(name=cls.__name__, fields=new_annotations_flat, bases=(OutputModel,), kw_only=True)



# Marker class to indicate that a type should skip JSON schema generation
class ExcludeFromJsonSchema(PreconfiguredBaseModel):
    pass

@excludes_json_schema
class MyModel(PreconfiguredBaseModel):
    a: int | bool | ExcludeFromJsonSchema
    b: int

# data = {"a": [{"field": 123}, {"field": 456}, {"field": 789}], "b": 42}
data = {"a": {"field": 123}, "b": 42}
data = {"a": 123, "b": 42}

# schema = json.schema(MyModel, schema_hook=schema_hook)
schema = MyModel.schema_json()

decoded = msgspec.convert(obj=data, type=MyModel, dec_hook=dec_hook_hf26)

pass
