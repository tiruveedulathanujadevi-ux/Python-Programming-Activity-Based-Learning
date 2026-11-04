
# Retail Billing System with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

# Get product details
product = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

# Calculate total amount
total = price * quantity
discount = 0

# Discount Rule 1: 10% discount for purchases above Rs.1000
if total >= 1000:
    discount += total * 0.10

# Discount Rule 2: Additional 5% for purchases above Rs.5000
if total >= 5000:
    discount += total * 0.05

# Discount Rule 3: Additional 2% for bulk purchases
if quantity >= 10:
    discount += total * 0.02

# Calculate final amount
final_amount = total - discount

# Display bill
print("\n========== CUSTOMER BILL ==========")
print("Product Name :", product)
print("Price        : Rs.", price)
print("Quantity     :", quantity)
print("-----------------------------------")
print("Total Amount : Rs.", total)
print("Discount     : Rs.", discount)
print("Final Amount : Rs.", final_amount)
print("===================================")
print("Thank You! Visit Again.")
