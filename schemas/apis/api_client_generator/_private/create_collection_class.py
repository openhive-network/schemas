from __future__ import annotations

import ast
from typing import Iterable

from schemas.apis.api_client_generator._private.common.converters import camel_to_snake


def create_api_collection(collection_name: str, api_client_classes: Iterable[ast.ClassDef]) -> ast.ClassDef:
    """
    Creates a collection class for the given API client classes.

    Args:
        collection_name(str): The name of the collection class.
        api_client_classes(Iterable[ast.ClassDef]): An iterable of API client class definitions.

    Example:
        create_api_collection("MyCollection", [FirstApiClientClass, SecondApiClientClass])

        output:
            class MyCollection:
                def __init__(self):
                    super().__init__()
                    self.first_api_client_class = FirstApiClientClass
                    self.second_api_client_class = SecondApiClientClass
    """
    init_method = ast.FunctionDef(  # type: ignore[call-overload]
        name="__init__",
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg="self")],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[],
        ),
        body=[
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Call(func=ast.Name(id="super", ctx=ast.Load()), args=[], keywords=[]),
                        attr="__init__",
                        ctx=ast.Load(),
                    ),
                    args=[],
                    keywords=[],
                )
            )
        ]
        + [
            ast.Assign(
                targets=[
                    ast.Attribute(
                        value=ast.Name(id="self", ctx=ast.Load()), attr=camel_to_snake(api_client.name), ctx=ast.Store()
                    )
                ],
                value=ast.Name(id=api_client.name, ctx=ast.Load()),
            )
            for api_client in api_client_classes
        ],
        decorator_list=[],
    )

    return ast.ClassDef(
        name=collection_name,
        bases=[],
        keywords=[],
        body=[init_method],
        decorator_list=[],
        type_params=[],
    )
