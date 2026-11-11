select *
from {{ ref('stg_payments') }}
where payment_amount < 0