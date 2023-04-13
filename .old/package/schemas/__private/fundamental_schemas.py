from __future__ import annotations

from abc import ABC, abstractmethod
import pprint
from typing import Any, Dict, List, Optional

from jsonschema.exceptions import ValidationError

from schemas.__private import custom_validator


class Schema(ABC):
    def __init__(self, **options: Any):
        self._options = options

    def __repr__(self) -> str:
        return str(self._create_schema())

    def validate(self, instance) -> None:
        custom_validator.validate(
            instance=instance,
            schema=self._create_schema(),
        )

    @abstractmethod
    def _create_core_of_schema(self) -> Dict[str, Any]:
        """
        This function create the core of the schema. Core is not a complete schema, it can't be validated.
        To pass validation, _create_schema adds basic schema parts and optional parameters (e.g 'enum', 'minItems'),
        creating a complete schema prepared for validation.
        """
        pass

    def _create_schema(self) -> Dict[str, Any]:
        return {**self._create_core_of_schema(), **self._options}

    @staticmethod
    def _assert_that_schema_has_correct_type(schema):
        if not isinstance(schema, Schema):
            raise ValidationError(f'Passed schema has invalid format:\n'
                                  f'{pprint.pformat(schema, indent=4, sort_dicts=False)}\n'
                                  f'\n'
                                  f'Instead you should use predefined schema, like: Int(), Str(), Map(), etc.\n'
                                  f'You can see examples in following files:\n'
                                  f'  schemas/tests/test_fundamental_schemas.py\n'
                                  f'  schemas/tests/test_custom_schemas.py\n'
                                  f'\n'
                                  f'You can check all available types here:\n'
                                  f'  schemas/package/schemas/predefined.py')

    def __eq__(self, other: Schema):
        """This is helper method which allows schemas testing."""
        return self._create_schema() == other._create_schema()


class AllOf(Schema):
    """
    AllOf: (AND) The instance must be valid for all of the subschemas
    Documentation: http://json-schema.org/understanding-json-schema/reference/combining.html#allof
    """
    def __init__(self, *items, **options: Any):
        super().__init__(**options)
        self.__items = list(items)

    def _create_core_of_schema(self) -> Dict[str, Any]:
        items_as_dicts = []
        for schema in self.__items:
            self._assert_that_schema_has_correct_type(schema)
            items_as_dicts.append(schema._create_schema())

        return {
            'allOf': items_as_dicts
        }


class AnyOf(Schema):
    """
    AnyOf: (OR) The instance must be valid for any (one or more) of the given subschemas
    Documentation: http://json-schema.org/understanding-json-schema/reference/combining.html#anyof
    """
    def __init__(self, *items, **options: Any):
        super().__init__(**options)
        self.__items = list(items)

    def __getitem__(self, key: int):
        return self.__items[key]

    def __len__(self):
        return len(self.__items)

    def __setitem__(self, key, value):
        self.__items[key] = value

    def _create_core_of_schema(self) -> Dict[str, Any]:
        items_as_dicts = []
        for schema in self.__items:
            self._assert_that_schema_has_correct_type(schema)
            items_as_dicts.append(schema._create_schema())

        return {
            'anyOf': items_as_dicts
        }


class Any_(Schema):
    """
    Accepts everything. Can be used to skip instance checking.
    """
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {}


class ArrayBase(ABC):
    """
    Base Array class for Array and ArrayStrict with dunder methods. It can't be instanciated or validated.
    """

    def __init__(self):
        self._items = list()

    def __delitem__(self, index):
        del self._items[index]

    def __getitem__(self, key: int):
        return self._items[key]

    def __len__(self):
        return len(self._items)

    def __setitem__(self, key, value):
        self._items[key] = value

    @abstractmethod
    def insert(self, index: Optional[int], schema: Schema) -> None:
        """
        Method for inserting new elements to _items attribute. It is possible to insert element on specified index by
        giving 'index' parameter. Without given 'index' new element is appended to list.
        """
        pass


class Array(Schema, ArrayBase):
    def __init__(self, item: Schema, *items: Schema, unique_items=False, **options: Any):
        """
        Ensures that given instance is an array and contains items of required types, e.g.:
        - Array(Int()) -> read as array of ints. [0, 1, 2, 1024],
        - Array(Str()) -> read as array of strings. ['a', 'b', 'c'],
        - Array(Str(), Int()) -> read as array of ints and strings. [0, 'a', 1, 'b'] - mixing of types is allowed,
        - Array(Any(), maxItems=0) -> if you want to validate always an empty array.
        Documentation: http://json-schema.org/understanding-json-schema/reference/array.html
        :param unique_items: Duplicated items in array are treated as error.
        """
        super().__init__(**options)
        self._items: List[Schema] = [item, *items]
        self.__unique_items = unique_items

    def _create_core_of_schema(self) -> Dict[str, Any]:
        items_as_dicts = []
        for schema in self._items:
            self._assert_that_schema_has_correct_type(schema)
            items_as_dicts.append(schema._create_schema())

        common_part_of_schema = {
            'type': 'array',
            'uniqueItems': self.__unique_items,
        }

        if len(items_as_dicts) > 1:
            return {
                **common_part_of_schema,
                'items': {
                    'oneOf': items_as_dicts,
                },
            }

        return {
            **common_part_of_schema,
            'items': items_as_dicts[0],
        }

    def insert(self, index: int, schema: Schema):
        if index is not None:
            raise RuntimeError('You tried to add element to array in specified index, this operation has no effect.'
                               'If sequence of elements is important, use ArrayStrict.')
        else:
            self._items.append(schema)


class ArrayStrict(Schema, ArrayBase):
    """
    Array Strict checks that the nth element in the instance, matches the nth type specified in the schema.
    example_array =  [0, 'string', True]
    example_schema : ArrayStrict(Int(), String(), Bool())
        example_array[0] -> Int(),
        example_array[1] -> String(),
        example_array[2] -> Bool()
    The ArrayStrict is the equivalent of a jsonschema tuple-validation:
        http://json-schema.org/understanding-json-schema/reference/array.html#tuple-validation
    The options available for Array can be used in ArrayStrict:
        http://json-schema.org/understanding-json-schema/reference/array.html
    """
    def __init__(self, *items, **options: Any):
        super().__init__(**options)
        self._items = list(items)

    def _create_core_of_schema(self) -> Dict[str, Any]:
        items_as_dicts = self._items.copy()
        for index, schema in enumerate(items_as_dicts):
            self._assert_that_schema_has_correct_type(schema)
            items_as_dicts[index] = schema._create_schema()

        return {
            'type': 'array',
            'prefixItems': items_as_dicts,
            "minItems": len(items_as_dicts),
            'maxItems': len(items_as_dicts),
        }

    def insert(self, index: int, schema: Schema):
        if index:
            self._items.insert(index, schema)
        else:
            self._items.append(schema)


class Bool(Schema):
    """
    Documentation: http://json-schema.org/understanding-json-schema/reference/boolean.html
    """
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {'type': 'boolean'}


class Date(Schema):
    """
    Date format used in HIVE ('%Y-%m-%dT%H:%M:%S').
    """
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {'type': 'hive-datetime'}


class Float(Schema):
    """
    Documentation: http://json-schema.org/understanding-json-schema/reference/numeric.html#number
    """
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {'type': 'number'}


class Int(Schema):
    """
    Validates normal JSON ints (e.g. 1, 42, -100), and also converted to strings
    (e.g. '1', '42', '-100'). All Hive APIs use this int format.
    """
    def __init__(self, **options: Any):
        super().__init__(**self.__replace_overridden_options(options))

    @staticmethod
    def __replace_overridden_options(options: Dict[str, Any]):
        validators_to_change = ['multipleOf', 'minimum', 'maximum', 'exclusiveMinimum', 'exclusiveMaximum']
        return {f'HiveInt.{k}' if k in validators_to_change else k: v for k, v in options.items()}

    def _create_core_of_schema(self) -> [str, Any]:
        return {'type': 'hive-int'}


class Json(Schema):
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {'type': 'json'}


class Map(Schema):
    def __init__(self, schema: Dict, required_keys: Optional[List[str]] = None,
                 allow_additional_properties: bool = False, optional_keys: Optional[List[str]] = None, **options: Any):
        """
        Validates JSON objects (in Python they are called dicts).
        :param schema: Collection of properties. Each of the individual properties has a key
        (represents the name of the key in instance), and schema (represents the required type,
        for the previously specified key).
        :param required_keys: The keys contained in this parameter are required for successful validation.
        The other keys specified in the schema are optional, their absence will not affect the validation process.
        :param allow_additional_properties: By default map does not accept additional undefined properties.
        All instance elements not defined in the schema will be reported as a 'ValidationError'.
        Set this parameter to True, it will allow the correct validation of additional properties in the instance.
        :param optional_keys: In this parameter you can specify which keys can be optional.
        :param options: Other options that can be given in the form of a dictionary.
        Documentation: http://json-schema.org/understanding-json-schema/reference/object.html
        """
        super().__init__(**options)
        self.__allow_additional_properties: bool = allow_additional_properties
        self.__schema = schema
        self.__required_keys: List[str] = list(self.__schema.keys()) if required_keys is None else required_keys
        if optional_keys is not None and required_keys is not None:
            raise RuntimeError("Options `optional_keys` and `required_keys` cannot be combined.")
        if optional_keys is not None:
            if isinstance(optional_keys, list) and len(optional_keys) == 0:
                raise RuntimeError("Options `optional_keys` must be specified. Provide key that exists in the schema")
            self.__required_keys = list(set(self.__required_keys).difference(set(optional_keys)))

    def __delitem__(self, key):
        self.__required_keys.remove(key)
        return self.__schema.__delitem__(key)

    def __getitem__(self, key):
        return self.__schema[key]

    def __setitem__(self, key: str, schema: Schema):
        number_or_elements_before_assigning = len(self.__schema.keys())
        self.__schema[key] = schema
        number_of_elements_after_assigning = len(self.__schema.keys())
        if number_or_elements_before_assigning != number_of_elements_after_assigning:
            self.__required_keys.append(key)

    def keys(self) -> list:
        return list(self.__schema.keys())

    def _create_core_of_schema(self) -> Dict[str, Any]:
        items_as_dicts = self.__schema.copy()
        for key, schema in self.__schema.items():
            self._assert_that_schema_has_correct_type(schema)
            items_as_dicts[key] = schema._create_schema()
        return {
            'type': 'object',
            'properties': items_as_dicts,
            'required': self.__required_keys,
            'additionalProperties': self.__allow_additional_properties
        }


class Null(Schema):
    """
    Documentation: http://json-schema.org/understanding-json-schema/reference/null.html
    """
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {'type': 'null'}


class OneOf(Schema):
    """
    OneOf: (XOR) The instance must be valid for exactly one of the given subschemas.
    Documentation: http://json-schema.org/understanding-json-schema/reference/combining.html#oneof
    """
    def __init__(self, *items, **options: Any):
        super().__init__(**options)
        self.__items = list(items)

    def _create_core_of_schema(self) -> Dict[str, Any]:
        items_as_dicts = []
        for schema in self.__items:
            self._assert_that_schema_has_correct_type(schema)
            items_as_dicts.append(schema._create_schema())

        return {
            'oneOf': items_as_dicts
        }


class Str(Schema):
    """
    Documentation: http://json-schema.org/understanding-json-schema/reference/string.html
    """
    def _create_core_of_schema(self) -> Dict[str, Any]:
        return {'type': 'string'}