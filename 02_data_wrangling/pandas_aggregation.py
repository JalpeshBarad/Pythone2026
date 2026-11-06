# 02_data_wrangling/pandas_aggregation.py
import pandas as pd

# 1. Create a simulated dataset (like a small database table)
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'category': ['Electronics', 'Home', 'Electronics', 'Books', 'Home', 'Electronics'],
    'amount': [120.00, 45.50, 300.00, 89.99, 210.00, 150.00]
}

df = pd.DataFrame(data)

print("--- Original Raw Data ---")
print(df)
print("\n" + "="*40 + "\n")

# 2. Pandas Equivalent of SQL GROUP BY (Total spend per category)
# This collapses rows, exactly like SUM() with GROUP BY!
category_summary = df.groupby('category')['amount'].sum().reset_index()
category_summary.rename(columns={'amount': 'total_revenue'}, inplace=True)

print("--- Aggregated Output (SQL GROUP BY Equivalent) ---")
print(category_summary)