select
    c.customer_id,
    c.customer_name,
    c.email,
    c.country,
    coalesce(o.order_count, 0) as order_count
from {{ ref('stg_customers') }} c
left join {{ ref('int_customer_orders') }} o
    on c.customer_id = o.customer_id
