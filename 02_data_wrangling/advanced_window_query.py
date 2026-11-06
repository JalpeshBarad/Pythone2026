# 02_data_wrangling/advanced_window_query.py
import duckdb
import pandas as pd

# 1. Simulate transaction data
transactions = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05', '2026-01-06'],
    'amount': [120.00, 45.50, 300.00, 89.99, 210.00, 150.00]
})

# 2. Modern SQL Window Function: Rank purchases per customer by amount
query = """
    SELECT 
        customer_id,
        order_date,
        amount,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) as spend_rank
    FROM transactions
"""

ranked_df = duckdb.sql(query).df()

print("--- Ranked Customer Transactions (Window Function Output) ---")
print(ranked_df)