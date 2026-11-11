from faker import Faker
import pandas as pd
import random

fake = Faker()

# -----------------
# CUSTOMERS
# -----------------

customers = []

for customer_id in range(1, 10001):
    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "registration_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)

# -----------------
# DATA QUALITY ISSUES
# -----------------

# 50 missing emails
missing_email_rows = random.sample(
    range(len(customers_df)),
    50
)

customers_df.loc[
    missing_email_rows,
    "email"
] = None

# 25 duplicate emails
for i in range(25):
    customers_df.loc[
        100 + i,
        "email"
    ] = customers_df.loc[i, "email"]

customers_df.to_csv(
    "seeds/customers.csv",
    index=False
)

# -----------------
# PRODUCTS
# -----------------

categories = [
    "Electronics",
    "Books",
    "Beauty",
    "Fashion",
    "Home"
]

products = []

for product_id in range(1, 1001):
    products.append({
        "product_id": product_id,
        "product_name": fake.word().title(),
        "category": random.choice(categories),
        "price": round(random.uniform(5, 1000), 2)
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "seeds/products.csv",
    index=False
)

# -----------------
# ORDERS
# -----------------

orders = []

for order_id in range(1, 100001):
    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1, 10000),
        "order_status": random.choice(
            ["completed", "pending", "cancelled"]
        )
    })

orders_df = pd.DataFrame(orders)

# 20 invalid statuses
invalid_status_rows = random.sample(
    range(len(orders_df)),
    20
)

orders_df.loc[
    invalid_status_rows,
    "order_status"
] = "invalid_status"

orders_df.to_csv(
    "seeds/orders.csv",
    index=False
)

# -----------------
# ORDER ITEMS
# -----------------

order_items = []

for item_id in range(1, 300001):

    order_items.append({
        "order_item_id": item_id,
        "order_id": random.randint(1, 100000),
        "product_id": random.randint(1, 1000),
        "quantity": random.randint(1, 5)
    })

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "seeds/order_items.csv",
    index=False
)

# -----------------
# PAYMENTS
# -----------------

payments = []

for payment_id in range(1, 100001):

    payments.append({
        "payment_id": payment_id,
        "order_id": random.randint(1, 100000),
        "payment_amount": round(
            random.uniform(10, 5000),
            2
        ),
        "payment_method": random.choice([
            "Credit Card",
            "PayPal",
            "Bank Transfer"
        ])
    })

payments_df = pd.DataFrame(payments)

# 100 negative payments
negative_rows = random.sample(
    range(len(payments_df)),
    100
)

payments_df.loc[
    negative_rows,
    "payment_amount"
] = -100

payments_df.to_csv(
    "seeds/payments.csv",
    index=False
)

print("All datasets generated successfully!")

