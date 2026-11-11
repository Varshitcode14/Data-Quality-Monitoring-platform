select
    payment_id,
    order_id,
    payment_amount,
    payment_method
from {{ ref('payments') }}
