from schemas.predefined import *

get_key_references = Map({
    'accounts': Array(
        Array(AccountName())
    )
})
