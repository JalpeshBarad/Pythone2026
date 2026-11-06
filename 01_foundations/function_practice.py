# 01_foundations/function_practice.py

def analyze_purchases(purchases):
    """
    A custom function that takes a list of purchases,
    categorizes them, and returns the total count of high-value sales.
    """
    high_value_count = 0
    
    for amount in purchases:
        if amount > 100:
            high_value_count += 1
            
    return high_value_count

# Here is our raw data list
store_sales = [45.50, 120.00, 15.75, 89.99, 210.40, 310.00]

# Now we call our custom function and store the result
total_high_value = analyze_purchases(store_sales)

# Print the final outcome
print(f"Out of {len(store_sales)} total purchases, {total_high_value} were High-Value sales.")