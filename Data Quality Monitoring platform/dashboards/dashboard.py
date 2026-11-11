import duckdb
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Data Quality Monitoring Platform",
    layout="wide"
)

conn = duckdb.connect("dbt.duckdb")

missing_emails = conn.execute("""
select count(*)
from dim_customers
where email is null
""").fetchone()[0]

duplicate_emails = conn.execute("""
select count(*)
from (
    select email
    from dim_customers
    where email is not null
    group by email
    having count(*) > 1
)
""").fetchone()[0]

invalid_statuses = conn.execute("""
select count(*)
from fct_orders
where order_status not in (
    'completed',
    'pending',
    'cancelled'
)
""").fetchone()[0]

negative_payments = conn.execute("""
select count(*)
from stg_payments
where payment_amount < 0
""").fetchone()[0]

customers_count = conn.execute("""
select count(*)
from dim_customers
""").fetchone()[0]

orders_count = conn.execute("""
select count(*)
from fct_orders
""").fetchone()[0]

total_issues = (
    missing_emails
    + duplicate_emails
    + invalid_statuses
    + negative_payments
)

dq_score = round(
    (
        1 -
        (
            total_issues /
            (customers_count + orders_count)
        )
    ) * 100,
    2
)

st.title("Data Quality Monitoring Platform")
st.caption("dbt - DuckDB - Streamlit - Plotly")

tab1, tab2, tab3 = st.tabs(
    [
        "Business Analytics",
        "Data Quality",
        "Investigation Center"
    ]
)

with tab1:

    st.subheader("Business Overview")

    revenue_by_category = conn.execute("""
    select
        category,
        sum(revenue) as revenue
    from fct_sales
    group by category
    order by revenue desc
    """).df()

    treemap = px.treemap(
        revenue_by_category,
        path=["category"],
        values="revenue",
        title="Revenue by Category"
    )

    treemap.update_traces(
        hovertemplate="<b>%{label}</b><br>Revenue: $%{value:,.0f}<extra></extra>"
    )

    st.plotly_chart(treemap, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        top_products = conn.execute("""
        select
            product_name,
            round(sum(revenue),2) as revenue
        from fct_sales
        group by product_name
        order by revenue desc
        limit 10
        """).df()

        fig_products = px.bar(
            top_products,
            x="revenue",
            y="product_name",
            orientation="h",
            title="Top 10 Products by Revenue",
            color="revenue"
        )

        st.plotly_chart(fig_products, use_container_width=True)

    with col2:

        countries = conn.execute("""
        select
            country,
            count(*) as customers
        from dim_customers
        group by country
        order by customers desc
        limit 15
        """).df()

        fig_country = px.bar(
            countries,
            x="customers",
            y="country",
            orientation="h",
            title="Top Countries by Customer Base",
            color="customers"
        )

        st.plotly_chart(fig_country, use_container_width=True)

with tab2:

    st.subheader("Data Quality Overview")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("DQ Score", f"{dq_score}%")
    c2.metric("Missing Emails", missing_emails)
    c3.metric("Duplicate Emails", duplicate_emails)
    c4.metric("Invalid Statuses", invalid_statuses)
    c5.metric("Negative Payments", negative_payments)

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=dq_score,
            title={"text": "Data Quality Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2563eb"},
                "steps": [
                    {"range": [0, 80], "color": "#fecaca"},
                    {"range": [80, 95], "color": "#fde68a"},
                    {"range": [95, 100], "color": "#bbf7d0"}
                ]
            }
        )
    )

    st.plotly_chart(gauge, use_container_width=True)

    findings = pd.DataFrame({
        "Issue": [
            "Duplicate Emails",
            "Negative Payments",
            "Missing Emails",
            "Invalid Statuses"
        ],
        "Count": [
            duplicate_emails,
            negative_payments,
            missing_emails,
            invalid_statuses
        ]
    })

    heatmap = px.imshow(
        [findings["Count"].tolist()],
        x=findings["Issue"],
        y=["Detected Issues"],
        text_auto=True,
        color_continuous_scale="Reds",
        title="Data Quality Findings"
    )

    st.plotly_chart(heatmap, use_container_width=True)

    payments = conn.execute("""
    select payment_amount
    from stg_payments
    """).df()

    col1, col2 = st.columns(2)

    with col1:

        box = px.box(
            payments,
            y="payment_amount",
            title="Payment Outlier Detection"
        )

        st.plotly_chart(box, use_container_width=True)

    with col2:

        hist = px.histogram(
            payments,
            x="payment_amount",
            nbins=50,
            title="Payment Amount Distribution"
        )

        st.plotly_chart(hist, use_container_width=True)

    failed_tests = pd.DataFrame({
        "Test": [
            "Missing Emails",
            "Duplicate Emails",
            "Invalid Statuses",
            "Negative Payments"
        ],
        "Failed Rows": [
            missing_emails,
            duplicate_emails,
            invalid_statuses,
            negative_payments
        ]
    })

    st.subheader("Failed Test Summary")

    st.dataframe(failed_tests, use_container_width=True)

with tab3:

    st.subheader("Investigation Center")

    st.markdown("### Missing Customer Emails")

    missing = conn.execute("""
    select
        customer_id,
        customer_name,
        country
    from dim_customers
    where email is null
    order by customer_id
    """).df()

    st.dataframe(missing, use_container_width=True)

    st.markdown("### Duplicate Emails")

    duplicates = conn.execute("""
    select
        email,
        count(*) as occurrences
    from dim_customers
    where email is not null
    group by email
    having count(*) > 1
    order by occurrences desc
    """).df()

    st.dataframe(duplicates, use_container_width=True)

    st.markdown("### Invalid Order Statuses")

    invalid_orders = conn.execute("""
    select
        order_id,
        customer_id,
        order_status
    from fct_orders
    where order_status not in (
        'completed',
        'pending',
        'cancelled'
    )
    """).df()

    st.dataframe(invalid_orders, use_container_width=True)

    st.markdown("### Negative Payments")

    negative = conn.execute("""
    select
        payment_id,
        order_id,
        payment_amount,
        payment_method
    from stg_payments
    where payment_amount < 0
    order by payment_id
    """).df()

    st.dataframe(negative, use_container_width=True)