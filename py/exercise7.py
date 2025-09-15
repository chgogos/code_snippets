inventory = ["sword", "potion", "potion", "shield"]

def add_item(inv, item):
    inv.append(item)
    print("Added:", item)

def use_item(inv, item):
    """Χρησιμοποιεί (αφαιρεί) ένα αντικείμενο από το inventory αν υπάρχει."""
    if item in inv:
        inv.remove(item)
        print("Used:", item)
    else:
        print(f"No {item} left to use.")

def show_inventory(inv):
    """Εμφανίζει το inventory και πόσες φορές εμφανίζεται κάθε αντικείμενο."""
    print("Inventory summary:")
    counted = {}
    for item in inv:
        counted[item] = counted.get(item, 0) + 1
    for item, count in counted.items():
        print(f"{item}: {count}")
    print("Full inventory:", inv)

add_item(inventory, "potion")  # Προσθήκη potion
use_item(inventory, "potion")  # Χρήση ενός potion
show_inventory(inventory)  # Εμφάνιση inventory
