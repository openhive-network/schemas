from schemas.__private.fundamental_schemas import Schema
from schemas.predefined import *


def get_schema(source: Schema, path: str) -> Schema:
    if path == 'source':
        return source

    # convert path
    path = path.split('.')
    wanted_element = source

    for element in path:
        if isinstance(wanted_element, Map):
            wanted_element = wanted_element[f'{element}']
        elif isinstance(wanted_element, (Array, ArrayStrict, AnyOf)):
            wanted_element = wanted_element[int(element)]
    return wanted_element
