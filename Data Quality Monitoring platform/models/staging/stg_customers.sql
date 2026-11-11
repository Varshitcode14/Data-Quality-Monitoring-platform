select
    customer_id,
    customer_name,
    lower(email) as email,
    country,
    registration_date
from {{ ref('customers') }}