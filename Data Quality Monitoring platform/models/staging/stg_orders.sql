select
    order_id,
    customer_id,
    order_status
from {{ ref('orders') }}