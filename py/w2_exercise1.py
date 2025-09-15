def calculate_total(price, quantity=1, discount=0):
    """Υπολογισμός συνολικού κόστους λαμβάνοντας υπόψη τιμή, ποσότητα και έκπτωση."""
    subtotal = price * quantity
    total = subtotal * (1 - discount / 100)
    return total

print(f"{calculate_total(75):.2f}") # 75.00
print(f"{calculate_total(75, 3, 12):.2f}") # 198.00
price = float(input("Τιμή μονάδας: "))

quantity_input = input("Ποσότητα (enter για 1): ")
if quantity_input.strip() == "":
    quantity = 1
else:
    quantity = int(quantity_input)

discount_input = input("Έκπτωση (enter για 0): ")
if discount_input.strip() == "":
    discount = 0
else:
    discount = float(discount_input)

total_cost = calculate_total(price, quantity, discount)
print(f"Σύνολο: {total_cost}")
