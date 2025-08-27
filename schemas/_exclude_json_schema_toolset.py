from __future__ import annotations

import typing
from dataclasses import dataclass

import msgspec

if typing.TYPE_CHECKING:
    from schemas._preconfigured_base_model import PreconfiguredBaseModel

FieldDictT = dict[str, msgspec.inspect.Field]
Exclusions = set[str]
NestedTypes = (
    msgspec.inspect.SetType
    | msgspec.inspect.ListType
    | msgspec.inspect.DictType
    | msgspec.inspect.TupleType
    | msgspec.inspect.UnionType
)


def _get_preconfigured_base_model_cls() -> type[PreconfiguredBaseModel]:
    from schemas._preconfigured_base_model import PreconfiguredBaseModel

    return PreconfiguredBaseModel


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


def recreate_struct(annotations: dict[str, type[typing.Any]], cls_name: str) -> type[typing.Any]:
    return msgspec.defstruct(
        name=cls_name, fields=list(annotations.items()), bases=(_get_preconfigured_base_model_cls(),), kw_only=True
    )


@dataclass(frozen=True)
class SlicedType:
    origin: type[NestedTypes] | None
    types_to_process: list[msgspec.inspect.Type]

    def compose_final_type(self, replaced_types: list[type[typing.Any]]) -> type[typing.Any]:
        if self.origin is not None:
            match self.origin:
                case msgspec.inspect.SetType:
                    return typing.Set[replaced_types[0]]  # type: ignore[valid-type]
                case msgspec.inspect.ListType:
                    return typing.List[replaced_types[0]]  # type: ignore[valid-type]
                case msgspec.inspect.DictType:
                    return typing.Dict[replaced_types[0], replaced_types[1]]  # type: ignore[valid-type]
                case msgspec.inspect.TupleType:
                    return typing.Tuple[tuple(replaced_types)]  # type: ignore[return-value]
                case msgspec.inspect.UnionType:
                    return typing.Union[tuple(replaced_types)]  # type: ignore[return-value]
                case _:
                    raise ValueError(f"Unsupported origin type: {self.origin}")
        assert len(replaced_types) == 1
        return replaced_types[0]


def slice_type(tp: msgspec.inspect.Type) -> SlicedType:
    if isinstance(tp, (msgspec.inspect.SetType, msgspec.inspect.ListType)):
        return SlicedType(origin=type(tp), types_to_process=[tp.item_type])
    if isinstance(tp, msgspec.inspect.DictType):
        return SlicedType(origin=type(tp), types_to_process=[tp.key_type, tp.value_type])
    if isinstance(tp, msgspec.inspect.TupleType):
        return SlicedType(origin=type(tp), types_to_process=list(tp.item_types))
    if isinstance(tp, msgspec.inspect.UnionType):
        return SlicedType(origin=type(tp), types_to_process=list(tp.types))
    return SlicedType(origin=None, types_to_process=[tp])


def recursive_type_replace(
    exclusions: Exclusions, annotations: FieldDictT, cls_name: str, cache: dict[str, type[typing.Any]]
) -> type[typing.Any]:
    if cls_name in cache:
        return cache[cls_name]

    final_annotations: dict[str, type[typing.Any]] = {}

    for field_name, field in annotations.items():
        if field_name in exclusions:
            continue

        if not isinstance(field.type, NestedTypes | msgspec.inspect.StructType):
            final_annotations[field_name] = _convert_type_to_annotation(field.type)
            continue

        sliced = slice_type(field.type)
        types_to_replace: list[type[typing.Any]] = []
        for tp in sliced.types_to_process:
            if isinstance(tp, msgspec.inspect.StructType) and issubclass(tp.cls, _get_preconfigured_base_model_cls()):
                types_to_replace.append(
                    recursive_type_replace(
                        exclusions=tp.cls.excluded_fields_for_schema_json(),
                        annotations=convert_field_list_to_dict(tp.fields),
                        cls_name=tp.cls.__name__,
                        cache=cache,
                    )
                )
                continue
            types_to_replace.append(_convert_type_to_annotation(tp))
        final_annotations[field_name] = sliced.compose_final_type(types_to_replace)

    result = recreate_struct(final_annotations, cls_name)
    cache[cls_name] = result
    return result


def convert_field_list_to_dict(field_list: tuple[msgspec.inspect.Field, ...]) -> FieldDictT:
    return {field.name: field for field in field_list}
