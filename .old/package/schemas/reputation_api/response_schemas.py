from schemas.predefined import *

get_account_reputations = Map({
    'reputations': Array(
        Map({
            'account': AccountName(),
            'reputation': Int(),
        })
    )
})
