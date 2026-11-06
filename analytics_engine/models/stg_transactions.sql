-- analytics_engine/models/stg_transactions.sql

SELECT 
    transaction_id,
    customer_id,
    category,
    amount,
    order_date
FROM read_csv_auto('../data/raw/raw_transactions.csv')
WHERE amount > 0