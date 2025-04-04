from __future__ import annotations

import ast
from typing import Iterable

from schemas.apis.api_client_generator._private.common.converters import camel_to_snake


def create_collection_class(collection_name: str, api_client_classes: Iterable[ast.ClassDef]) -> ast.ClassDef:
    """
    Creates a collection class for the given API client classes.

    Args:
        collection_name: The name of the collection class.
        api_client_classes An iterable of API client class definitions.

    Example:
        create_collection_class("MyCollection", [FirstApiClientClass, SecondApiClientClass])

        output:
            class MyCollection:
                def __init__(self):
                    super().__init__()
                    self.first_api_client_class = FirstApiClientClass
                    self.second_api_client_class = SecondApiClientClass
    """
    init_body: list[ast.stmt] = [
        ast.Assign(
            targets=[
                ast.Attribute(
                    value=ast.Name(
                        id="self",
                    ),
                    attr=camel_to_snake(api_client.name),
                )
            ],
            value=ast.Name(id=api_client.name),
        )
        for api_client in api_client_classes
    ]

    class_body: list[ast.stmt] = [
        ast.FunctionDef(
            name="__init__",
            args=ast.arguments(
                posonlyargs=[],
                args=[ast.arg(arg="self")],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=init_body,
            decorator_list=[],
            returns=None,
            type_params=[],
        )
    ]

    return ast.ClassDef(
        name=collection_name,
        bases=[],
        keywords=[],
        body=class_body,
        decorator_list=[],
        type_params=[],
    )
