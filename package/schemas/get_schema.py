import importlib


def get_schema(schema_name):
    api, method = schema_name.split('.')
    schemas_module = importlib.import_module(f'schemas.{api}')
    try:
        return getattr(schemas_module, method)
    except:
        raise AttributeError(f'The \'{method}\' method in \'{api}\' api does not have a matching schema.'
                             f' This means that the schema does not exist.')
