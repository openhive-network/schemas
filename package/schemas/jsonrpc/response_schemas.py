from schemas.predefined import *

get_methods = Array(Str())

get_signature = Map({
<<<<<<< HEAD
    'args': Any(),
    'ret': Any(),
=======
    'args': AnyOf(
        Array(),
        Map({}, allow_additional_properties=True),
        Null(),
    ),
    'ret': AnyOf(
        Array(),
        Bool(),
        HardforkVersion(),
        Int(),
        Map({}, allow_additional_properties=True),
        Null(),
        Str(pattern=''),
    ),
>>>>>>> 2a73928 (Add schemas to `jsonrpc` API)
})
