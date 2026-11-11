select
    'Missing Emails' as issue_type,
    count(*) as issue_count
from {{ ref('dim_customers') }}
where email is null

union all

select
    'Negative Payments',
    count(*)
from {{ ref('stg_payments') }}
where payment_amount < 0

select 'Missing Emails' as issue,
       count(*) as count
from {{ ref('dim_customers') }}
where email is null