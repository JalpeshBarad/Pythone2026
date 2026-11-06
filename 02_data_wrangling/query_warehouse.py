# 02_data_wrangling/query_warehouse.py
import duckdb

# Connect to DuckDB (in-memory) and query our local "processed warehouse" files directly
query = """
    SELECT 
        c.region,
        t.category,
        COUNT(t.transaction_id) AS total_orders,
        SUM(t.amount) AS regional_revenue,
        AVG(t.amount) AS avg_order_value
    FROM 'data/processed/fct_transactions.csv' AS t
    JOIN 'data/processed/dim_customers.csv' AS c
        ON t.customer_id = c.customer_id
    GROUP BY c.region, t.category
    ORDER BY regional_revenue DESC
"""

# Execute the query and convert results directly to a pandas dataframe
result_df = duckdb.sql(query).df()

print("--- Regional Sales & Category Performance (Warehouse Query) ---")
print(result_df)