# Data Quality & Analytics Monitoring Platform

An end-to-end analytics engineering solution designed to simulate a real-world e-commerce data environment, transform raw datasets into business-ready models, and continuously monitor data quality.

Built using **dbt Core, DuckDB, Python, Streamlit, and Plotly**, the platform combines structured data transformation, automated validation, anomaly detection, and interactive analytics into a unified monitoring system.

## Overview

Data quality plays a critical role in reliable business intelligence and decision-making. This project addresses common data reliability challenges by introducing a layered analytics architecture with automated validation and data investigation capabilities.

The platform generates synthetic e-commerce data, processes it through multiple dbt transformation layers, identifies inconsistencies using automated tests, and presents actionable insights through an interactive dashboard.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python, SQL |
| Data Processing | Pandas, Faker |
| Data Warehouse | DuckDB |
| Analytics Engineering | dbt Core |
| Visualization | Streamlit, Plotly |
| Data Validation | dbt Tests, Custom SQL Tests |

## System Architecture

The platform follows a modular ELT (Extract, Load, Transform) workflow.

```text
       Synthetic Data Generation
                  |
                  v
             CSV Datasets
                  |
                  v
          DuckDB Data Warehouse
                  |
                  v
          dbt Staging Models
                  |
                  v
        Intermediate Transformations
                  |
                  v
             Analytics Marts
                  |
                  v
          Automated Quality Tests
                  |
                  v
       Interactive Monitoring Dashboard
                  |
          +-------+-------+
          |               |
          v               v
    Business Insights   Data Investigation
```

## Project Structure

```text
dbt-analytics-project/
│
├── analyses/
│
├── dashboards/
│   └── dashboard.py
│
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
│
├── seeds/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── payments.csv
│
├── tests/
│
├── dbt_project.yml
├── profiles.yml
├── generate_data.py
└── README.md
```

## Dataset Overview

The project uses synthetically generated e-commerce datasets to replicate realistic transactional data at scale.

| Dataset | Number of Records |
|---|---:|
| Customers | 10,000 |
| Products | 1,000 |
| Orders | 100,000 |
| Order Items | 300,000 |
| Payments | 100,000 |
| **Total** | **511,000** |

## Data Transformation Pipeline

The dbt project follows a three-layer modeling approach to ensure maintainability, reusability, and consistency.

### 1. Staging Layer

Handles initial data preparation, standardization, and cleaning.

- `stg_customers`
- `stg_products`
- `stg_orders`
- `stg_order_items`
- `stg_payments`

### 2. Intermediate Layer

Implements business logic and combines data across multiple entities.

- `int_customer_orders`
- `int_product_sales`

### 3. Analytics Marts

Creates business-ready dimensional and fact models for reporting and analysis.

- `dim_customers`
- `dim_products`
- `fct_orders`
- `fct_sales`

## Automated Data Quality Framework

A key component of the platform is its automated data validation framework, implemented using dbt's testing capabilities.

**Built-in validations:**
- `not_null` – Identifies missing values in critical columns.
- `unique` – Detects duplicate records and identifiers.
- `accepted_values` – Validates categorical fields against predefined values.

**Custom validation:**
- `payment_amount_positive` – Identifies invalid payment transactions with non-positive amounts.

### Simulated Data Quality Issues

To evaluate the monitoring system, controlled data inconsistencies are intentionally injected into the generated datasets.

| Data Quality Issue | Injected Records |
|---|---:|
| Missing Customer Emails | 50 |
| Duplicate Customer Emails | 210 |
| Invalid Order Statuses | 20 |
| Negative Payment Amounts | 100 |

These records serve as test cases for validating the platform's detection and investigation capabilities.

## Interactive Monitoring Dashboard

The Streamlit dashboard provides a consolidated view of business performance and data reliability.

### Business Analytics

- Revenue distribution across product categories.
- Highest-performing products based on revenue.
- Customer distribution across countries.
- Key business performance indicators.

### Data Quality Monitoring

- Overall data quality score.
- Quality-related KPI tracking.
- Failed validation test summaries.
- Payment anomaly and outlier detection.
- Payment distribution analysis.
- Detailed data quality findings.

### Data Investigation Center

Provides record-level visibility into detected data issues.

- Missing customer email investigation.
- Duplicate email identification.
- Invalid order status investigation.
- Negative payment transaction investigation.

## Screenshots & Visualizations

### dbt Model Lineage

Visual representation of dependencies and transformations across the analytics pipeline.

![dbt Lineage](image.png)

### Business Analytics

![Business Analytics](image-9.png)

![Business Analytics](image-10.png)

### Data Quality Monitoring

![Data Quality Dashboard](image-1.png)

![Data Quality Dashboard](image-2.png)

![Data Quality Dashboard](image-3.png)

![Data Quality Dashboard](image-4.png)

### Data Investigation Center

![Investigation Center](image-5.png)

![Investigation Center](image-6.png)

![Investigation Center](image-7.png)

![Investigation Center](image-8.png)

## Getting Started

### Prerequisites

- Python 3.10+
- dbt Core
- dbt-duckdb adapter

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd dbt-analytics-project
```

### 2. Install Dependencies

```bash
pip install pandas faker duckdb streamlit plotly
pip install dbt-core dbt-duckdb
```

### 3. Generate Synthetic Data

```bash
python generate_data.py
```

### 4. Execute dbt Models

```bash
dbt seed --profiles-dir .
dbt run --profiles-dir .
```

### 5. Run Data Quality Tests

```bash
dbt test --profiles-dir .
```

### 6. Generate dbt Documentation

```bash
dbt docs generate --profiles-dir .
dbt docs serve --profiles-dir .
```

### 7. Launch the Dashboard

```bash
streamlit run dashboards/dashboard.py
```

## Key Learning Outcomes

Through this project, the following concepts and engineering practices are demonstrated:

- Designing modular ELT pipelines using dbt.
- Building layered analytics models and dimensional data structures.
- Working with DuckDB as an analytical database.
- Implementing automated data quality validations.
- Detecting anomalies and investigating problematic records.
- Developing interactive dashboards for business and technical stakeholders.
- Connecting data engineering workflows with business intelligence applications.

## Author

**Kosuru Varshit**

B.Tech – Electrical Engineering  
Indian Institute of Technology Bhubaneswar

[GitHub](https://github.com/Varshitcode14)
