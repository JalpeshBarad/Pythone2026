# 01_foundations/sales_check.py

total_amount = 149.97

# Check if the total amount qualifies for a high-value purchase
if total_amount > 100:
    print(f"Total is ${total_amount}. This is a High-Value sale!")
else:
    print(f"Total is ${total_amount}. This is a Standard sale.")