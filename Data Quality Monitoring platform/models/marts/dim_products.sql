select
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    coalesce(
        s.total_quantity_sold,
        0
    ) as total_quantity_sold
from {{ ref('stg_products') }} p
left join {{ ref('int_product_sales') }} s
    on p.product_id = s.product_id
