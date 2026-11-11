with missing_emails as (

    select count(*) as cnt
    from {{ ref('dim_customers') }}
    where email is null

),

negative_payments as (

    select count(*) as cnt
    from {{ ref('stg_payments') }}
    where payment_amount < 0

)

select
    (select cnt from missing_emails) as missing_emails,
    (select cnt from negative_payments) as negative_payments