# 02_data_wrangling/generate_raw_data.py
import pandas as pd
import os

# Ensure the data/raw directory exists
os.makedirs('data/raw', exist_ok=True)

# 1. Simulate Raw Customer Table
customers_raw = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'signup_date': ['2026-01-10', '2026-01-12', '2026-01-15', '2026-01-18', '2026-01-20'],
    'region': ['North', 'South', 'East', 'West', 'North']
})

# 2. Simulate Raw Transaction Table (with some messy/uncleaned entries)
transactions_raw = pd.DataFrame({
    'transaction_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'customer_id': [101, 102, 101, 103, 999, 102, 104], # Note: 999 is an orphaned customer ID (messy data!)
    'category': ['Tech', 'Home', 'Tech', 'Books', 'Tech', 'Home', 'Tech'],
    'amount': [250.00, 45.00, 300.00, 120.50, -50.00, 210.00, 89.99], # Note: -50.00 is a bad record!
    'order_date': ['2026-02-01', '2026-02-01', '2026-02-02', '2026-02-03', '2026-02-04', '2026-02-05', '2026-02-06']
})

# Save them as raw CSV files into the data/raw/ directory
customers_raw.to_csv('data/raw/raw_customers.csv', index=False)
transactions_raw.to_csv('data/raw/raw_transactions.csv', index=False)

print("--- Success! Raw enterprise data generated and saved ---")
print("Files created:")
print("-> data/raw/raw_customers.csv")
print("-> data/raw/raw_transactions.csv")