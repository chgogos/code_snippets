person = {"name": "Νικόλαος", "age": 26}

# get(): επιστρέφει τιμή κλειδιού ή None (ή default αν δοθεί)
print("Όνομα:", person.get("name"))  # Νικόλαος
print("Χώρα:", person.get("country"))  # None
print("Χώρα (με default):", person.get("country", "Ελλάδα"))  # Ελλάδα

# pop(): αφαιρεί και επιστρέφει την τιμή ενός κλειδιού
age = person.pop("age")
print("Ηλικία που αφαιρέθηκε:", age)  # 26
print("Λεξικό μετά το pop:", person)  # {'name': 'Νικόλαος'}

# update(): ενημερώνει/προσθέτει ζεύγη από άλλο λεξικό
person.update({"city": "Αθήνα", "job": "Μηχανικός"})
print("Μετά το update:", person)
# {'name': 'Νικόλαος', 'city': 'Αθήνα', 'job': 'Μηχανικός'}

# clear(): διαγράφει όλα τα ζεύγη
person.clear()
print("Μετά το clear:", person)  # {}
