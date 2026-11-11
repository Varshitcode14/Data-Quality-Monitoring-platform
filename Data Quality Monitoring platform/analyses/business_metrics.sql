select
    category,
    round(sum(revenue), 2) as total_revenue
from {{ ref('fct_sales') }}
group by category
order by total_revenue desc