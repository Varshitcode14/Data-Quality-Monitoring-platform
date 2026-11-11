select
    product_id,
    sum(quantity) as total_quantity_sold
from {{ ref('stg_order_items') }}
group by product_id