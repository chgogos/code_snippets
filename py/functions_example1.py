# Συνάρτηση που επιστρέφει μια τιμή
def calculate_area(length, width):
    area = length * width
    return area  

# Κλήση συνάρτησης calculate_area()
room_area = calculate_area(4.5, 3.2)
print(f"Το εμβαδόν είναι: {room_area} τ.μ.")


# Συνάρτηση που δεν επιστρέφει τιμή
def print_greeting(name):
    print(f"Γεια σου {name}!")

# Κλήση συνάρτησης που δεν επιστρέφει τιμή
print_greeting("Μαρία")  

result = print_greeting("Ελένη")
print("Αποτέλεσμα:", result)  # Θα εκτυπωθεί "Αποτέλεσμα: None"
