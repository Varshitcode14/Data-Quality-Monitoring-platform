select
    category,
    sum(revenue) as revenue
from {{ ref('fct_sales') }}
group by category
order by revenue desc

select
    category,
    sum(revenue) as revenue
from {{ ref('fct_sales') }}
group by category
