# 02_data_wrangling/clean_raw_data.py
import pandas as pd
import os

# Ensure processed directory exists
os.makedirs('data/processed', exist_ok=True)

# 1. Load the raw files we generated earlier
customers_df = pd.read_csv('data/raw/raw_customers.csv')
transactions_df = pd.read_csv('data/raw/raw_transactions.csv')

print(f"--- Loaded Raw Data ---")
print(f"Raw Transactions Count: {len(transactions_df)}")

# 2. Data Cleaning Rules (The ELT Transformation Step)
# Rule A: Remove negative amounts (bad records/refund anomalies)
clean_transactions = transactions_df[transactions_df['amount'] > 0].copy()

# Rule B: Remove orphaned transactions where the customer doesn't exist in the customer table
clean_transactions = clean_transactions[clean_transactions['customer_id'].isin(customers_df['customer_id'])].copy()

print(f"Transactions after cleaning: {len(clean_transactions)}")

# 3. Save the cleaned tables into the data/processed/ folder
customers_df.to_csv('data/processed/dim_customers.csv', index=False)
clean_transactions.to_csv('data/processed/fct_transactions.csv', index=False)

print("\n--- Success! Processed enterprise tables saved ---")
print("-> data/processed/dim_customers.csv")
print("-> data/processed/fct_transactions.csv")