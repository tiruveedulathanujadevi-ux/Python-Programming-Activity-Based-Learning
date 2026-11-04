
# Tuple-Based Product Catalogue Audit

print("===== PRODUCT CATALOGUE AUDIT =====")

# Store product details using tuples
products = (
    ("Laptop", 50000, 10),
    ("Mobile", 20000, 15),
    ("Keyboard", 1500, 20),
    ("Mouse", 800, 25),
    ("Monitor", 12000, 8)
)

total_products = len(products)
total_stock_value = 0

# Display product catalogue
print("\nProduct Catalogue Details")

for product in products:
    name, price, quantity = product

    stock_value = price * quantity
    total_stock_value += stock_value

    print("\nProduct Name:", name)
    print("Price: Rs.", price)
    print("Quantity:", quantity)
    print("Stock Value: Rs.", stock_value)

    if quantity < 10:
        print("Stock Status: Low Stock")
    else:
        print("Stock Status: Available")

# Calculate total stock value
print("\n===== CATALOGUE AUDIT REPORT =====")

print("Total Products:", total_products)
print("Total Stock Value: Rs.", total_stock_value)

# Find the most expensive product
expensive_product = max(products, key=lambda x: x[1])

print("Most Expensive Product:",
      expensive_product[0])
print("Highest Price: Rs.", expensive_product[1])

print("\n===== AUDIT COMPLETED =====")
