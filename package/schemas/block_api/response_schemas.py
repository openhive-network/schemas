from schemas.predefined import *

<<<<<<< HEAD
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

=======
get_block = AnyOf(
    Map({}),
    Map({
        'block': Map({
            'block_id': TransactionId(),
            'previous': TransactionId(),
            'extensions': Any(),
            'signing_key': PublicKey(),
            'timestamp': Date(),
            'transaction_ids': Array(TransactionId()),
            'transactions': Any(),
            'transaction_merkle_root': TransactionId(),
            'witness': AccountName(),
            'witness_signature': Signature(),
        })

    })
)
>>>>>>> 59571a4 (Add schemas to `block` API)

get_block_header = AnyOf(
    Map({}),
    Map({
        'header': Map({
<<<<<<< HEAD
            'extensions': Array(Any()),
=======
            'extensions': Array(),
>>>>>>> 59571a4 (Add schemas to `block` API)
            'previous': TransactionId(),
            'timestamp': Date(),
            'transaction_merkle_root': TransactionId(),
            'witness': AccountName(),
        })
    })
)

get_block_range = Map({
<<<<<<< HEAD
    'blocks': Array(__BLOCK)
=======
    'blocks': Array(
        Map({
            'block_id': TransactionId(),
            'extensions': Array(),
            'previous': TransactionId(),
            'signing_key': PublicKey(),
            'timestamp': Date(),
            'transaction_ids': Array(TransactionId()),
            'transaction_merkle_root': TransactionId(),
            'transactions': Array(),
            'witness': AccountName(),
            'witness_signature': Signature(),
        })
    )
>>>>>>> 59571a4 (Add schemas to `block` API)
})
