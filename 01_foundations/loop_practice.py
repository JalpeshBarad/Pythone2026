# 01_foundations/loop_practice.py

# A list of multiple purchase amounts
purchase_list = [45.50, 120.00, 15.75, 89.99, 210.40]

print("Processing individual purchases:")

# A 'for' loop goes through each amount in the list one by one
for amount in purchase_list:
    if amount > 100:
        print(f"-> ${amount} is a High-Value sale.")
    else:
        print(f"-> ${amount} is a Standard sale.")