def process_order(item_name, quantity, price, tax_rate, express_shipping):
    total = quantity * price * (1 + tax_rate)
    if express_shipping:
        total += 10
    print(f"Παραγγελία: {quantity} x {item_name} = {total:.2f}€")


# Μόνο ορίσματα θέσης
process_order("Φορητός Η/Υ", 1, 999.99, 0.24, True)

# Μίξη ορισμάτων θέσης και ονοματισμένων ορισμάτων
process_order("Κινητό", 2, 599.99, express_shipping=True, tax_rate=0.24)

# process_order(tax_rate=0.24, "Κινητό", 2, 599.99, express_shipping=True) # S
