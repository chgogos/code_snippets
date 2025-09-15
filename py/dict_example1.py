person = {}

person["name"] = "Alice"
person["age"] = 25
person["city"] = "Athens"
print("Αρχικό λεξικό:", person)
# {'name': 'Alice', 'age': 25, 'city': 'Athens'}

# Τροποποίηση στοιχείου του λεξικού
person["age"] = 26
print("Μετά την τροποποίηση:", person)
# {'name': 'Alice', 'age': 26, 'city': 'Athens'}

# Πρόσβαση σε στοιχείο του λεξικού
print("Η ηλικία είναι:", person["age"])  # 26

# Διαγραφή στοιχείου του λεξικού με del
del person["city"]
print("Μετά τη διαγραφή του city:", person)
# {'name': 'Alice', 'age': 26}

print(person["city"])  # KeyError
