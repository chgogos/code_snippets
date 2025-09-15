phrase = "hello world"

# Με χρήση [] (απαιτεί αρχικοποίηση)
count_brackets = {}
for c in phrase:
    if c not in count_brackets:
        count_brackets[c] = 0
    count_brackets[c] += 1
print("Using []:", count_brackets)

# Με χρήση.get() (απλούστερο)
count_get = {}
for c in phrase:
    count_get[c] = count_get.get(c, 0) + 1
print("Using .get():", count_get)
