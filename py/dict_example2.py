person = {"name": "Nikolaos", "age": 26, "city": "Athens"}

print("Keys:", person.keys())  
# dict_keys(['name', 'age', 'city'])

print("Values:", person.values())  
# dict_values(['Alice', 26, 'Athens'])

print(
    "Items:", person.items()
)  
# dict_items([('name', 'Alice'), ('age', 26), ('city', 'Athens')])
print("-" * 20)
for key in person.keys():
    print(key)
print("-" * 20)
for value in person.values():
    print(value)
print("-" * 20)
for key, value in person.items():
    print(f"{key}: {value}")
