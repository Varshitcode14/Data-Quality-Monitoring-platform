select
    country,
    count(*) as customer_count,
    avg(order_count) as avg_orders
from {{ ref('dim_customers') }}
group by country
order by customer_count desc

select
    country,
    count(*) as customers,
    avg(order_count) as avg_orders
from {{ ref('dim_customers') }}
group by country