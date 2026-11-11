select
    oi.order_id,
    oi.product_id,
    o.customer_id,
    p.product_name,
    p.category,
    oi.quantity,
    p.price,
    oi.quantity * p.price as revenue,
    o.order_status
from {{ ref('stg_order_items') }} oi

left join {{ ref('stg_orders') }} o
    on oi.order_id = o.order_id

left join {{ ref('stg_products') }} p
    on oi.product_id = p.product_id