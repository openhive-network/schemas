from __future__ import annotations

import typing

import msgspec


def _convert_type_to_annotation(tp: msgspec.inspect.Type) -> type:
    if isinstance(tp, msgspec.inspect.CustomType | msgspec.inspect.NoneType):
        return type(None)
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
    return typing.Any
