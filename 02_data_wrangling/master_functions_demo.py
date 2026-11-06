# 02_data_wrangling/master_functions_demo.py
import duckdb
import pandas as pd

# 1. Create a Master Dataset of Store Transactions
# This table has enough rows and variety to test every single function.
transactions = pd.DataFrame({
    'transaction_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'customer_id': [101, 101, 102, 102, 101, 103, 103, 102],
    'category': ['Tech', 'Tech', 'Home', 'Home', 'Tech', 'Home', 'Home', 'Tech'],
    'amount': [100.00, 250.00, 50.00, 150.00, 300.00, 80.00, 120.00, 200.00],
    'order_date': [
        '2026-01-01', '2026-01-02', '2026-01-03', 
        '2026-01-04', '2026-01-05', '2026-01-06', 
        '2026-01-07', '2026-01-08'
    ]
})

print("=== ORIGINAL MASTER DATASET (8 Rows) ===")
print(transactions)
print("\n" + "="*50 + "\n")


# ==========================================
# PART 1: AGGREGATE FUNCTIONS (GROUP BY)
# Result: COLLAPSES rows into summary metrics per group.
# ==========================================

agg_query = """
    SELECT 
        category,
        COUNT(transaction_id) AS total_orders,
        SUM(amount) AS total_revenue,
        AVG(amount) AS avg_order_amount,
        MAX(amount) AS max_purchase,
        MIN(amount) AS min_purchase
    FROM transactions
    GROUP BY category
"""

agg_result = duckdb.sql(agg_query).df()
print("=== 1. AGGREGATE FUNCTIONS OUTPUT (Collapsed to 2 rows by Category) ===")
print(agg_result)
print("\n" + "="*50 + "\n")


# ==========================================
# PART 2: WINDOW FUNCTIONS (OVER)
# Result: KEEPS ALL ORIGINAL ROWS (8 rows), adding calculated columns side-by-side.
# ==========================================

window_query = """
    SELECT 
        transaction_id,
        customer_id,
        category,
        amount,
        -- 1. RANKING: Rank customer's purchases by amount (highest first)
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS customer_spend_rank,
        
        -- 2. TREND / VALUE: Look at the previous transaction amount for that customer
        LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order_amount,
        
        -- 3. AGGREGATE WINDOW: Running total of customer spend over time
        SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS customer_running_total
    FROM transactions
    ORDER BY customer_id, order_date
"""

window_result = duckdb.sql(window_query).df()
print("=== 2. WINDOW FUNCTIONS OUTPUT (All 8 original rows kept intact) ===")
print(window_result)