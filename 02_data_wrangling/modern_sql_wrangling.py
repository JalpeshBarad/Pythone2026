# 02_data_wrangling/modern_sql_wrangling.py
import duckdb
import pandas as pd

# 1. Raw sales data (simulating a 1,000,000-row transactional table)
raw_sales = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102, 101, 104],
    'category': ['Tech', 'Home', 'Tech', 'Tech', 'Home', 'Tech', 'Home'],
    'amount': [1200.00, 150.50, 450.00, 89.99, 210.00, 99.00, 45.00]
})

# 2. Modern Technique: Querying DataFrames or Files directly with SQL inside Python
query = """
    SELECT 
        category,
        COUNT(customer_id) AS total_orders,
        SUM(amount) AS total_revenue,
        AVG(amount) AS avg_order_value
    FROM raw_sales
    WHERE amount > 50
    GROUP BY category
    ORDER BY total_revenue DESC
"""

# Run the SQL query using DuckDB's in-memory engine
summary_df = duckdb.query(query).to_df()

print("--- Modern SQL Aggregation Output ---")
print(summary_df)