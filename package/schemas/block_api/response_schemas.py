from schemas.predefined import *

__BLOCK = Map({
    'block_id': TransactionId(),
    'extensions': Array(Any()),
    'previous': TransactionId(),
    'signing_key': PublicKey(),
    'timestamp': Date(),
    'transaction_ids': Array(TransactionId()),
    'transaction_merkle_root': TransactionId(),
    'transactions': Array(Any()),
    'witness': AccountName(),
    'witness_signature': Signature(),
})

get_block = AnyOf(
    Map({}),
    Map({'block': __BLOCK})
)


get_block_header = AnyOf(
    Map({}),
    Map({
        'header': Map({
            'extensions': Array(Any()),
            'previous': TransactionId(),
            'timestamp': Date(),
            'transaction_merkle_root': TransactionId(),
            'witness': AccountName(),
        })
    })
)

get_block_range = Map({
    'blocks': Array(__BLOCK)
})
