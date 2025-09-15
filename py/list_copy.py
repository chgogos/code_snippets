a_list = [1, 2, 3]

# Αντιγραφή αναφοράς (δημιουργία ενός ψευδωνύμου = alias)
new_list = a_list
new_list.append(4)
print(a_list)    # [1, 2, 3, 4] => η a_list επηρεάζεται
print(new_list)  # [1, 2, 3, 4]

# Πραγματική αντιγραφή (με slice)
a_list = [1, 2, 3]
new_list = a_list[:]
new_list.append(4)
print(a_list)    # [1, 2, 3] => η a_list δεν επηρεάζεται
print(new_list)  # [1, 2, 3, 4]
