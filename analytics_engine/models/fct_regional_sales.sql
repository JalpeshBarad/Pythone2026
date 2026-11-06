-- analytics_engine/models/fct_regional_sales.sql

WITH cleaned_transactions AS (
    SELECT * FROM {{ ref('stg_transactions') }}
),

customers AS (
    SELECT * FROM read_csv_auto('../data/raw/raw_customers.csv')
)

SELECT 
    c.region,
    t.category,
    COUNT(t.transaction_id) AS total_orders,
    SUM(t.amount) AS regional_revenue,
    AVG(t.amount) AS avg_order_value
FROM cleaned_transactions AS t
JOIN customers AS c
    ON t.customer_id = c.customer_id
GROUP BY c.region, t.category
ORDER BY regional_revenue DESC