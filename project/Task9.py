products = [
    {"name": "Mechanical Keyboard", "price": 3499.00, "stock": 12},
    {"name": "USB Hub", "price": 899.50, "stock": 0},
    {"name": "Monitor Stand", "price": 1250.75, "stock": 5},
    {"name": "Webcam", "price": 2199.00, "stock": 3},
] 

print(f"{'Product':<20} {'Price (₹)':<15} {'Stock':<10} Status")

print("-" * 55)

for product in products:
    if product["stock"] > 0:
        Status = "Available"
    else :
        Status = "Out Of Stock"

    print(f"{product['name']:<20}" 
      f"{product['price']:<15}"
      f"{product['stock']:<10}"
      f"{Status}"
      )